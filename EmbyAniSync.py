from __future__ import print_function

from config import emby_settings, item_service, settings, users
import logging
import json

from embypython import BaseItemDto

import anilist
import embymodule
import graphql
from custom_mappings import read_custom_mappings
from embyclasses import EmbyShow, EmbyWatchedSeries, EmbySeason
from apscheduler.schedulers.background import BackgroundScheduler
# app.py

from flask import Flask, request

logger = logging.getLogger("EmbyAniSync")
scheduler = BackgroundScheduler()

app = Flask(__name__)


# webhook from emby
@app.route('/update_show', methods=['POST'])
def update_anilist():
    data = json.loads(dict(request.form)['data'])

    if 'Item' not in data:
        print('not an episode finished! Probably a test!')
        return '200'
    item = data['Item']
    user = data['User']
    user_id = user['Id']
    user_name = user['Name']
    # pprint(data)

    # pprint(data['Item'])
    series = item_service.get_items(ids=item['SeriesId'] + ',' + item['SeasonId'], include_item_types='Series,Season',
                                    enable_user_data=True, user_id=user_id,
                                    fields='ProviderIds,RecursiveItemCount,SortName,ProductionYear')

    emby_show: EmbyShow

    #This will always be Series first!
    for item in series.items:
        item: BaseItemDto
        # cleaned = clean_nones(item.to_dict())
        # pprint(cleaned)
        match item.type:
            case 'Series':
                emby_show = EmbyShow(item)
            case 'Season':
                emby_show.seasons.append(EmbySeason(item))

    emby_watched_series: EmbyWatchedSeries = EmbyWatchedSeries(
        emby_show.name.strip(),
        emby_show.sort_name.strip(),
        emby_show.name.strip(),
        emby_show.year,
        emby_show.seasons,
        emby_show.anilist_id
    )

    anilist.CUSTOM_MAPPINGS = read_custom_mappings()

    if graphql.ANILIST_SKIP_UPDATE:
        logger.warning(
            "AniList skip list update enabled in settings, will match but NOT update your list"
        )

    if anilist.ANILIST_EMBY_EPISODE_COUNT_PRIORITY:
        logger.warning(
            "Emby episode watched count will take priority over AniList, this will always update AniList watched count over Emby data"
        )

    anilist.clean_failed_matches_file()

    # Anilist
    user_config = settings['users.' + user_name]
    anilist_username = user_config.get('anilist_username')
    anilist_token = user_config.get('anilist_token')

    anilist_series = anilist.process_user_list(anilist_username, anilist_token)

    anilist.match_to_emby(anilist_series, [emby_watched_series], anilist_token)

    logger.info("Emby to AniList sync finished")
    return '200'


#cron to update everything
@scheduler.scheduled_job(trigger='interval', hours=4)
def update_all():
    # pprint(data)
    # pprint(data['Item'])
    anilist.CUSTOM_MAPPINGS = read_custom_mappings()

    if graphql.ANILIST_SKIP_UPDATE:
        logger.warning(
            "AniList skip list update enabled in settings, will match but NOT update your list"
        )

    if anilist.ANILIST_EMBY_EPISODE_COUNT_PRIORITY:
        logger.warning(
            "Emby episode watched count will take priority over AniList, this will always update AniList watched count over Emby data"
        )

    anilist.clean_failed_matches_file()

    for user in users:
        user_config = settings['users.' + user]
        if 'anilist_token' not in user_config:
            continue
        emby_user_id = user_config.get('emby_user_id')
        anilist_username = user_config.get('anilist_username')
        anilist_token = user_config.get('anilist_token')

        emby_anime_series = []

        for library in emby_settings.get('anime_section_ids').split(','):
            embymodule.get_anime_shows(emby_anime_series, library, emby_user_id)

        emby_series_watched = embymodule.get_watched_shows(emby_anime_series)

        anilist_series = anilist.process_user_list(anilist_username, anilist_token)

        if emby_series_watched is None:
            logger.error("Found no watched shows on Emby for processing")
        else:
            anilist.match_to_emby(anilist_series, emby_series_watched, anilist_token)

        logger.info("Emby to AniList sync finished for {}", anilist_username)
    return "200"


def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value


# update all on first run
update_all()

app.run(host='0.0.0.0', port=8081)

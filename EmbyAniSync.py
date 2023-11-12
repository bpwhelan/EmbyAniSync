from __future__ import print_function

import coloredlogs

from config import emby_settings, item_service, settings, users, general_settings
import json

from embypython import BaseItemDto

import anilist
import embymodule
import graphql
from custom_mappings import read_custom_mappings
from embyclasses import EmbyShow, EmbyWatchedSeries, EmbySeason, EmbyMovie, EmbyWatchedMovie

from flask import Flask, request

from flask_apscheduler import scheduler as apscheduler

import logging
from logging.handlers import RotatingFileHandler

LOG_FILENAME = "EmbyAniSync.log"
logger = logging.getLogger("EmbyAniSync")

# Add the rotating log message handler to the standard log
handler = RotatingFileHandler(
    LOG_FILENAME, maxBytes=10_000_000, backupCount=5, encoding="utf-8"
)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

# Debug log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[logging.FileHandler("EmbyAniSync-DEBUG.log", "w", "utf-8")],
)

# Install colored logs
coloredlogs.install(fmt="%(asctime)s %(message)s", logger=logger)

app = Flask(__name__)

logger.info('Server Started, Syncing first')

scheduler = apscheduler.BackgroundScheduler()


# webhook from emby
@app.route('/update_show', methods=['POST'])
def update_anilist():
    data = json.loads(dict(request.form)['data'])

    logger.debug(json.dumps(data))

    if 'Item' not in data:
        print('not an episode or movie finished! Probably a test!')
        return '200'
    item = data['Item']
    user = data['User']
    user_id = user['Id']
    user_name = user['Name']

    logger.info("Syncing based on new webhook! User: %s")
    # pprint(data)

    item_type = item.get('Type')

    if item_type == 'Series' or item_type == 'Season' or item_type == 'Episode':

        # pprint(data['Item'])
        series = item_service.get_items(ids=item['SeriesId'] + ',' + item['SeasonId'], include_item_types='Series,Season',
                                        enable_user_data=True, user_id=user_id,
                                        fields='ProviderIds,RecursiveItemCount,SortName,ProductionYear')

        emby_show: EmbyShow

        # This will always be Series first!
        for series_item in series.items:
            series_item: BaseItemDto
            # cleaned = clean_nones(item.to_dict())
            # pprint(cleaned)
            match series_item.type:
                case 'Series':
                    emby_show = EmbyShow(series_item)
                case 'Season':
                    emby_show.seasons.append(EmbySeason(series_item))

        emby_watched_series: EmbyWatchedSeries = EmbyWatchedSeries(
            emby_show.name.strip(),
            emby_show.sort_name.strip(),
            emby_show.name.strip(),
            emby_show.year,
            emby_show.seasons,
            emby_show.anilist_id
        )

        # Process series
        process_anilist_sync(user_name, [emby_watched_series])

    elif item_type == 'Movie':
        movie = item_service.get_items(ids=item['Id'], include_item_types='Movie',
                                       enable_user_data=True, user_id=user_id,
                                       fields='ProviderIds,SortName,ProductionYear')

        emby_movie: EmbyMovie

        for movie_item in movie.items:
            movie_item: BaseItemDto
            emby_movie = EmbyMovie(movie_item)

        emby_watched_movie: EmbyWatchedMovie = EmbyWatchedMovie(
            emby_movie.name.strip(),
            emby_movie.sort_name.strip(),
            emby_movie.name.strip(),  # Replace with emby_movie.originalTitle.strip() if using original titles
            emby_movie.year,
            emby_movie.anilist_id
        )

        # Process movies
        process_anilist_sync(user_name, [emby_watched_movie])

    else:
        logger.warning(f"Unknown item type: {item_type}")
        return '400', 'Unknown item type'

    logger.info("Emby to AniList sync finished")
    return '200'

def process_anilist_sync(user_name, emby_items):
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

    anilist_items = anilist.process_user_list(anilist_username, anilist_token)

    anilist.match_to_emby(anilist_items, emby_items, anilist_token)


# cron to update everything
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

    for user in users.users:
        emby_anime_series = []
        emby_anime_movies = []
        

        for library in emby_settings.anime_section_ids:
            embymodule.get_anime_shows(emby_anime_series, library, user.emby_user_id)
            embymodule.get_anime_movies(emby_anime_movies, library, user.emby_user_id)

        emby_series_watched = embymodule.get_watched_shows(emby_anime_series)
        emby_movies_watched = embymodule.get_watched_movies(emby_anime_movies)

        anilist_series = anilist.process_user_list(user.anilist_username, user.anilist_token)

        if emby_series_watched is None:
            logger.error("Found no watched shows on Emby for processing")
        else:
            anilist.match_to_emby(anilist_series, emby_series_watched, user.anilist_token)
        
        if emby_movies_watched is None:
            logger.error("Found no watched movies on Emby for processing")
        else:
            anilist.match_to_emby(anilist_series, emby_movies_watched, user.anilist_token)

        logger.info("Emby to AniList sync finished for %s", user.anilist_username)
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


scheduler.add_job(update_all, trigger='interval',
                  hours=general_settings.scheduler_timeout)
scheduler.start()

# update all on first run
update_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)

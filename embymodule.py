# coding=utf-8
import json
import logging
import re

import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

from embyclasses import *

logger = logging.getLogger("EmbyAniSync")
emby_settings = dict()


class HostNameIgnoringAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=..., **pool_kwargs):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       assert_hostname=False,
                                       **pool_kwargs)


# def authenticate() -> EmbyServer:
#     method = emby_settings["authentication_method"].lower()
#     try:
#         home_user_sync = emby_settings["home_user_sync"].lower()
#         home_username = emby_settings["home_username"]
#         home_server_base_url = emby_settings["home_server_base_url"]
#     except Exception:
#         home_user_sync = "false"
#         home_username = ""
#         home_server_base_url = ""
#
#     try:
#         session = Session()
#         session.mount("https://", HostNameIgnoringAdapter())
#
#         # Direct connection
#         if method == "direct":
#             base_url = emby_settings["base_url"]
#             token = emby_settings["token"]
#             emby = EmbyServer(base_url, token, session)
#
#         # Myemby connection
#         elif method == "myemby":
#             emby_server = emby_settings["server"]
#             emby_user = emby_settings["myemby_user"]
#             emby_password = emby_settings["myemby_password"]
#
#             if home_user_sync == "true":
#                 if home_username == "":
#                     logger.error(
#                         "Home authentication cancelled as home_username is empty"
#                     )
#                     sys.exit(1)
#
#                 logger.warning(
#                     f"Authenticating as admin f1or MyEmby home user: {home_username}"
#                 )
#                 # emby_account = MyEmbyAccount(emby_user, emby_password)
#                 emby_account = emby_settings.userID
#                 emby_server_home = EmbyServer(
#                     home_server_base_url, emby_account.authenticationToken, session
#                 )
#
#                 logger.warning("Retrieving home user information")
#                 emby_user_account = emby_account.user(home_username)
#
#                 logger.warning("Retrieving user token for MyEmby home user")
#                 emby_user_token = emby_user_account.get_token(
#                     emby_server_home.machineIdentifier
#                 )
#
#                 logger.warning("Retrieved user token for MyEmby home user")
#                 emby = EmbyServer(home_server_base_url, emby_user_token, session)
#                 logger.warning("Successfully authenticated for MyEmby home user")
#             else:
#                 account = MyEmbyAccount(emby_user, emby_password, session=session)
#                 emby = account.resource(emby_server).connect()
#         else:
#             logger.critical(
#                 "[EMBY] Failed to authenticate due to invalid settings or authentication info, exiting..."
#             )
#             sys.exit(1)
#         return emby
#     except Exception:
#         logger.exception("Unable to authenticate to Emby Media Server")
#         sys.exit(1)

def get_anime_shows(emby_shows: List[EmbyShow], anime_section_id) -> List[EmbyShow]:
    base_url = emby_settings["base_url"]
    token = emby_settings["token"]
    user_id = emby_settings["userID"]
    # anime_section_id = emby_settings["anime_section_id"]
    response = requests.get(
        base_url + "/emby/Users/" + user_id + "/Items?ParentId=" + anime_section_id + "&Fields=ProviderIds%2CRecursiveItemCount%2CSeasonCount%2CProductionYear&api_key=" + token)

    # print(response.content)

    data = json.loads(response.content)

    # print(data)
    # emby_shows = []
    for item in data["Items"]:
        # print(item)
        emby_shows.append(EmbyShow(item))
        # for key in item:
        #     print(key + ": " + str(type(item[key])))
        # break

    # for show in emby_shows:
    response = requests.get(
        base_url + "/emby/Users/" + user_id + "/Items?Recursive=true&ParentId=" + anime_section_id + "&Fields=ProviderIds%2CRecursiveItemCount%2CSortName%2CProductionYear&IncludeItemTypes=Season&EnableUserData=true&api_key=" + token)

    # print(response.content)
    data = json.loads(response.content)
    # print(data)

    all_seasons = []

    for season in data["Items"]:
        emby_season = EmbySeason(season)
        all_seasons.append(emby_season)
        matched_show = next((show for show in emby_shows if show.id == emby_season.series_id), None)
        if matched_show and emby_season.name.lower().startswith('season'):
            emby_season.parent_name = matched_show.name
            matched_show.seasons.append(emby_season)

    # print(next((show for show in emby_shows if show.name == "Attack on Titan"), None))
    # for key in item:
    #     print(key + ": " + str(type(item[key])))
    # break

    # sections = emby_settings["anime_section"].split("|")
    # shows: List[Show] = []
    # for section in sections:
    #     try:
    #         logger.info(f"[EMBY] Retrieving anime series from section: {section}")
    #         shows_search = emby.library.section(section.strip()).search()
    #         shows += shows_search
    #         logger.info(
    #             f"[EMBY] Found {len(shows_search)} anime series in section: {section}"
    #         )
    #     except BaseException:
    #         logger.error(
    #             f"Could not find library [{section}] on your Emby Server, check the library "
    #             "name in AniList settings file and also verify that your library "
    #             "name in Emby has no trailing spaces in it"
    #         )

    return emby_shows


def get_anime_shows_filter(show_name):
    shows = get_anime_shows()

    shows_filtered = []
    for show in shows:
        show_title_clean_without_year = show.name
        filter_title_clean_without_year = re.sub("[^A-Za-z0-9]+", "", show_name)
        show_title_clean_without_year = re.sub(r"\(\d{4}\)", "", show_title_clean_without_year)
        show_title_clean_without_year = re.sub("[^A-Za-z0-9]+", "", show_title_clean_without_year)

        if (show.title.lower().strip() == show_name.lower().strip()
                or show_title_clean_without_year.lower().strip() == filter_title_clean_without_year.lower().strip()):
            shows_filtered.append(show)

    if shows_filtered:
        logger.info("[EMBY] Found matching anime series")
    else:
        logger.info(f"[EMBY] Did not find {show_name} in anime series")
    return shows_filtered


def get_watched_shows(shows: List[EmbyShow]) -> Optional[List[EmbyWatchedSeries]]:
    logger.info("[EMBY] Retrieving watch count for series")
    watched_series: List[EmbyWatchedSeries] = []
    ovas_found = 0

    for show in shows:
        try:
            anilist_id = show.anilist_id

            if hasattr(show, "seasons"):
                show_seasons = show.seasons
                # ignore season 0 and unwatched seasons
                show_seasons = filter(lambda
                                          season: season.season_number is not None and season.season_number > 0 and season.episodes_played > 0,
                                      show_seasons)

                seasons = []
                for season in show_seasons:
                    seasons.append(season)

                if seasons:
                    # Add year if we have one otherwise fallback
                    year = 1900
                    if show.year:
                        year = int(show.year)

                    if not hasattr(show, "sort_name"):
                        show.sort_name = show.name
                    elif show.sort_name == "":
                        show.sort_name = show.name

                    # Disable original title for now, results in false positives for yet unknown reason

                    # if not hasattr(show, 'originalTitle'):
                    #    show.originalTitle = show.title
                    # elif show.originalTitle == '':
                    #    show.originalTitle = show.title
                    show.name = show.name

                    watched_show = EmbyWatchedSeries(
                        show.name.strip(),
                        show.name.strip(),
                        show.name.strip(),
                        year,
                        seasons,
                        anilist_id
                    )
                    watched_series.append(watched_show)

                    # logger.info(
                    #    'Watched %s episodes of show: %s' % (
                    #        episodes_watched, show.title))
            else:
                # Probably OVA but adding as series with 1 episode and season
                # Needs proper solution later on and requires changing AniList
                # class to support it properly

                if hasattr(show, "isWatched") and show.isWatched:
                    year = 1900
                    if show.year:
                        year = int(show.year)

                    if not hasattr(show, "sort_name"):
                        show.sort_name = show.name
                    elif show.titleSort == "":
                        show.sort_name = show.name

                    # Disable original title for now, results in false positives for yet unknown reason

                    # if not hasattr(show, 'originalTitle'):
                    #    show.originalTitle = show.title
                    # elif show.originalTitle == '':
                    #    show.originalTitle = show.title
                    # show.originalTitle = show.name

                    watched_show = EmbyWatchedSeries(
                        show.name.strip(),
                        show.sort_name.strip(),
                        show.name.strip(),
                        year,
                        [EmbySeason(1, 1)],
                        anilist_id
                    )
                    watched_series.append(watched_show)
                    ovas_found += 1
        except Exception:
            logger.exception(f"[EMBY] Error occured during episode processing of show {show}")

    logger.info(f"[EMBY] Found {len(watched_series)} watched series")

    if ovas_found > 0:
        logger.info(
            f"[EMBY] Watched series also contained {ovas_found} releases with no episode attribute (probably movie / OVA), "
            "support for this is still experimental"
        )

    if watched_series is not None and len(watched_series) == 0:
        return None
    else:
        return watched_series


def get_watched_episodes_for_show_season(season: EmbySeason) -> int:
    # watched_episodes_of_season: List[Episode] = season.watched()
    # len(watched_episodes_of_season) only works when the user didn't skip any episodes
    # episodes_watched = max(map(lambda e: int(e.index), watched_episodes_of_season), default=0)

    episodes_watched = season.episodes_played

    logger.info(f'[EMBY] {episodes_watched} episodes watched for {season.parent_name} season {season.season_number}')
    return episodes_watched

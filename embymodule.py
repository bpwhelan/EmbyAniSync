# coding=utf-8
import json
import logging
import re

import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from config import emby_settings, item_service

from embyclasses import *

logger = logging.getLogger("EmbyAniSync")


class HostNameIgnoringAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=..., **pool_kwargs):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       assert_hostname=False,
                                       **pool_kwargs)


def get_anime_shows(emby_shows: List[EmbyShow], anime_section_id, user_id: str) -> List[EmbyShow]:
    series = item_service.get_items(parent_id=anime_section_id, recursive=True, include_item_types='Series',
                                    enable_user_data=True, user_id=user_id,
                                    fields='ProviderIds,RecursiveItemCount,SortName,ProductionYear')
    for item in series.items:
        item: BaseItemDto
        emby_shows.append(EmbyShow(item))

    seasons = item_service.get_items(parent_id=anime_section_id, recursive=True, include_item_types='Season',
                                    enable_user_data=True, user_id=user_id,
                                    fields='ProviderIds,RecursiveItemCount,SortName,ProductionYear')
    all_seasons = []

    for season in seasons.items:
        emby_season = EmbySeason(season)
        all_seasons.append(emby_season)
        matched_show = next((show for show in emby_shows if show.id == emby_season.series_id), None)
        if matched_show and emby_season.name.lower().startswith('season'):
            emby_season.parent_name = matched_show.name
            matched_show.seasons.append(emby_season)

    return emby_shows


def get_anime_movies(emby_movies: List[EmbyMovie], anime_section_id, user_id: str) -> List[EmbyMovie]:
    movies = item_service.get_items(parent_id=anime_section_id, recursive=True, include_item_types='Movie',
                                    enable_user_data=True, user_id=user_id,
                                    fields='ProviderIds,SortName,ProductionYear')
    for item in movies.items:
        item: BaseItemDto
        emby_movies.append(EmbyMovie(item))

    return emby_movies


# Following two functions could be merged, but they don't seem to be used anywhere
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

def get_anime_movies_filter(movie_name):
    movies = get_anime_movies()

    movies_filtered = []
    for movie in movies:
        movie_title_clean_without_year = movie.name
        filter_title_clean_without_year = re.sub("[^A-Za-z0-9]+", "", movie_name)
        movie_title_clean_without_year = re.sub(r"\(\d{4}\)", "", movie_title_clean_without_year)
        movie_title_clean_without_year = re.sub("[^A-Za-z0-9]+", "", movie_title_clean_without_year)

        if (movie.title.lower().strip() == movie_name.lower().strip()
                or movie_title_clean_without_year.lower().strip() == filter_title_clean_without_year.lower().strip()):
            movies_filtered.append(movie)

    if movies_filtered:
        logger.info("[EMBY] Found matching anime movie")
    else:
        logger.info(f"[EMBY] Did not find {movie_name} in anime movies")
    return movies_filtered


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

def get_watched_movies(movies: List[EmbyMovie]) -> Optional[List[EmbyWatchedMovie]]:
    logger.info("[EMBY] Retrieving watch status for movies")
    watched_movies: List[EmbyWatchedMovie] = []

    for movie in movies:
        try:
            if hasattr(movie, "user_data") and movie.user_data.played:
                anilist_id = movie.anilist_id
                year = 1900  # fallback year
                if movie.year:
                    year = int(movie.year)

                if not hasattr(movie, "sort_name"):
                    movie.sort_name = movie.name
                elif movie.sort_name == "":
                    movie.sort_name = movie.name

                # The following section is commented out as it appears to be handling original titles,
                # similar to the commented out section in get_watched_shows.
                # Uncomment and adjust if needed.
                # if not hasattr(movie, 'originalTitle'):
                #    movie.originalTitle = movie.title
                # elif movie.originalTitle == '':
                #    movie.originalTitle = movie.title
                # movie.originalTitle = movie.name

                watched_movie = EmbyWatchedMovie(
                    movie.name.strip(),
                    movie.sort_name.strip(),
                    movie.name.strip(),  # Replace with movie.originalTitle.strip() if using original titles
                    year,
                    anilist_id
                )
                watched_movies.append(watched_movie)
        except Exception:
            logger.exception(f"[EMBY] Error occurred during processing of movie {movie}")

    logger.info(f"[EMBY] Found {len(watched_movies)} watched movies")

    if watched_movies is not None and len(watched_movies) == 0:
        return None
    else:
        return watched_movies

def get_watched_episodes_for_show_season(season: EmbySeason) -> int:
    episodes_watched = season.episodes_played

    logger.info(f'[EMBY] {episodes_watched} episodes watched for {season.parent_name} season {season.season_number}')
    return episodes_watched

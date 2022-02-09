# coding=utf-8
import configparser
import logging.handlers
import os
import sys

import coloredlogs

import anilist
import embymodule
import graphql
from _version import __version__
from custom_mappings import read_custom_mappings

# Logger settings
LOG_FILENAME = "EmbyAniSync.log"
logger = logging.getLogger("EmbyAniSync")

# Add the rotating log message handler to the standard log
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=10000000, backupCount=5, encoding="utf-8"
)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

# Debug log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("EmbyAniSync-DEBUG.log", "w", "utf-8")],
)

# Install colored logs
coloredlogs.install(fmt="%(asctime)s %(message)s", logger=logger)


# Enable this if you want to also log all messages coming from imported libraries
# coloredlogs.install(level='DEBUG')

## Settings section ##


def read_settings(settings_file) -> configparser.ConfigParser:
    if not os.path.isfile(settings_file):
        logger.critical(f"[CONFIG] Settings file file not found: {settings_file}")
        sys.exit(1)
    settings = configparser.ConfigParser()
    settings.read(settings_file, encoding="utf-8")
    return settings


SETTINGS_FILE = os.getenv("SETTINGS_FILE") or "settings.ini"

if len(sys.argv) > 1:
    SETTINGS_FILE = sys.argv[1]
    logger.warning(f"Found settings file parameter and using: {SETTINGS_FILE}")

settings = read_settings(SETTINGS_FILE)
anilist_settings = settings["ANILIST"]
emby_settings = settings["EMBY"]

graphql.ANILIST_ACCESS_TOKEN = anilist_settings["access_token"].strip()

if "skip_list_update" in anilist_settings:
    graphql.ANILIST_SKIP_UPDATE = anilist_settings["skip_list_update"].lower().strip() == "true"

if "emby_episode_count_priority" in anilist_settings:
    anilist.ANILIST_EMBY_EPISODE_COUNT_PRIORITY = (
        anilist_settings["emby_episode_count_priority"].lower().strip() == "true"
    )

if "log_failed_matches" in anilist_settings:
    anilist.ANILIST_LOG_FAILED_MATCHES = (
        anilist_settings["log_failed_matches"].lower().strip() == "true"
    )


## Startup section ##
def start():
    logger.info(f"EmbyAniSync - version: {__version__}")

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
    anilist_username = anilist_settings["username"]
    anilist_series = anilist.process_user_list(anilist_username)

    # Emby
    if anilist_series is None:
        logger.error(
            "Unable to retrieve AniList list, check your username and access token"
        )
    else:
        if not anilist_series:
            logger.error(
                "No items found on your AniList list for additional processing later on"
            )

        embymodule.emby_settings = emby_settings
        emby_anime_series = embymodule.get_anime_shows()

        # if emby_anime_series is None:
        #     logger.error("Found no Emby shows for processing")
        #     emby_series_watched = None
        # else:
        emby_series_watched = embymodule.get_watched_shows(emby_anime_series)

        if emby_series_watched is None:
            logger.error("Found no watched shows on Emby for processing")
        else:
            anilist.match_to_emby(anilist_series, emby_series_watched)

    logger.info("Emby to AniList sync finished")


if __name__ == "__main__":
    start()

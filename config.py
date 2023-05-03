import configparser
import logging
import os
import sys

import embypython
from embypython import UserItemDataDto, BaseItemDto
from embypython.rest import ApiException

logger = logging.getLogger("EmbyAniSync")

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
users = settings['users'].get('users').split(',')

configuration = embypython.Configuration()
configuration.host = emby_settings.get('url')
configuration.api_key['api_key'] = emby_settings.get('apikey')

client = embypython.ApiClient(configuration)

# create an instance of the API class
item_service = embypython.ItemsServiceApi(client)
user_service = embypython.UserLibraryServiceApi(client)
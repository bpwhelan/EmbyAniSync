import configparser
import logging
import os
import sys

import embypython
from dataclasses import dataclass
from configparser import SectionProxy, ConfigParser

logger = logging.getLogger("EmbyAniSync")


@dataclass
class GeneralSettings:
    scheduler_timeout: int = 12

    def __init__(self, config: SectionProxy):
        self.scheduler_timeout = int(config.get('sync_all_timer'), 12)


@dataclass
class EmbySettings:
    anime_section_ids: list[str]
    url: str
    apikey: str

    def __init__(self, config: SectionProxy):
        self.anime_section_ids = config.get('anime_section_ids').split(',')
        self.url = config.get('url')
        self.apikey = config.get('apikey')


@dataclass
class AnilistSettings:
    emby_episode_count_priority: bool = False
    skip_list_update: bool = False
    log_failed_matches: bool = True

    def __init__(self, config: SectionProxy):
        self.emby_episode_count_priority = bool(config.get('emby_episode_count_priority', 'False'))
        self.skip_list_update = bool(config.get('skip_list_update', 'False'))
        self.log_failed_matches = bool(config.get('log_failed_matches', 'False'))


@dataclass
class User:
    emby_user_id: str
    anilist_username: str
    anilist_token: str


@dataclass
class Users:
    users: list[User]

    def __init__(self, config: ConfigParser):
        self.users = []
        for user in config['users'].get('users').split(','):
            user_config = settings['users.' + user]
            if 'anilist_token' not in user_config:
                continue
            self.users.append(User(
                user_config.get('emby_user_id'),
                user_config.get('anilist_username'),
                user_config.get('anilist_token')
            ))


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
emby_settings = EmbySettings(settings["EMBY"])
general_settings = GeneralSettings(settings['general'])
users = Users(settings)

configuration = embypython.Configuration()
configuration.host = emby_settings.url
configuration.api_key['api_key'] = emby_settings.apikey

client = embypython.ApiClient(configuration)

# create an instance of the API class
item_service = embypython.ItemsServiceApi(client)
user_service = embypython.UserLibraryServiceApi(client)

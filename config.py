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
    """General application settings parsed from the [general] config section."""
    scheduler_timeout: int = 12

    def __init__(self, config: SectionProxy):
        """Initialize from a ConfigParser section proxy.

        Args:
            config: The [general] section of settings.ini.
        """
        self.scheduler_timeout = int(config.get('sync_all_timer'), 12)


@dataclass
class EmbySettings:
    """Emby server connection settings parsed from the [EMBY] config section."""
    anime_section_ids: list[str]
    url: str
    apikey: str

    def __init__(self, config: SectionProxy):
        """Initialize from a ConfigParser section proxy.

        Args:
            config: The [EMBY] section of settings.ini.
        """
        self.anime_section_ids = config.get('anime_section_ids').split(',')
        self.url = config.get('url')
        self.apikey = config.get('apikey')


@dataclass
class AnilistSettings:
    """AniList-specific settings parsed from the [ANILIST] config section."""
    emby_episode_count_priority: bool = False
    skip_list_update: bool = False
    log_failed_matches: bool = True

    def __init__(self, config: SectionProxy):
        """Initialize from a ConfigParser section proxy.

        Args:
            config: The [ANILIST] section of settings.ini.
        """
        self.emby_episode_count_priority = bool(config.get('emby_episode_count_priority', 'False'))
        self.skip_list_update = bool(config.get('skip_list_update', 'False'))
        self.log_failed_matches = bool(config.get('log_failed_matches', 'False'))


@dataclass
class User:
    """Represents a single user mapping between Emby and AniList accounts."""
    emby_user_id: str
    anilist_username: str
    anilist_token: str


@dataclass
class Users:
    """Collection of configured user mappings parsed from settings.ini."""
    users: list[User]

    def __init__(self, config: ConfigParser):
        """Parse all user entries from the config file.

        Args:
            config: The full ConfigParser instance containing [users] and [users.*] sections.
        """
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
    """Read and parse the INI settings file.

    Args:
        settings_file: Path to the settings.ini file.

    Returns:
        A populated ConfigParser instance.

    Raises:
        SystemExit: If the settings file does not exist.
    """
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

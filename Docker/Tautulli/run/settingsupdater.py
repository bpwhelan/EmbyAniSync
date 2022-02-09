import configparser
import os

config = configparser.ConfigParser()

config['EMBY'] = {
    'anime_section': os.environ.get('EMBY_SECTION'),
    'authentication_method': 'direct',
    'base_url': os.environ.get('EMBY_URL'),
    'token': os.environ.get('EMBY_TOKEN'),
}

config['ANILIST'] = {
    'username': os.environ.get('ANI_USERNAME'),
    'access_token': os.environ.get('ANI_TOKEN'),
    'emby_episode_count_priority': os.environ.get('EMBY_EPISODE_COUNT_PRIORITY', False),
    'skip_list_update': os.environ.get('SKIP_LIST_UPDATE', False),
    'log_failed_matches': os.environ.get('LOG_FAILED_MATCHES', False),
}

with open('/embyanisync/settings.ini', 'w', encoding="UTF-8") as configfile:
    config.write(configfile)

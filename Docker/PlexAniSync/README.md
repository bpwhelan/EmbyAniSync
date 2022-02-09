# Docker-EmbyAniSync

## Usage

### Docker Run

```
docker run -d \
  --name=embyanisync \
  --restart unless-stopped \
  -e EMBY_SECTION=Anime \
  -e EMBY_URL=http://127.0.0.1:32400 \
  -e EMBY_TOKEN=SomeEmbyToken \
  -e ANI_USERNAME=SomeUser \
  -e ANI_TOKEN=SomeToken \
  -e INTERVAL=3600 \
  -v /etc/localtime:/etc/localtime:ro \
  ghcr.io/rickdb/embyanisync:latest
```

### Environment Variables

| ID                          | Default                | Required | Note                                                                                                                                                     |
| --------------------------- | ---------------------- | :-------: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EMBY_SECTION                | Anime                  | &#10003;* | The library where your anime resides                                                                                                                     |
| EMBY_URL                    | http://127.0.0.1:32400 | &#10003;* | The address to your Emby Media Server, for example: http://127.0.0.1:32400                                                                               |
| EMBY_TOKEN                  | -                      | &#10003;* | Follow [this guide](https://support.emby.tv/articles/204059436-finding-an-authentication-token-x-emby-token/)                                            |
| ANI_USERNAME                | -                      | &#10003;* | Your [AniList.co](http://www.anilist.co) username                                                                                                        |
| ANI_TOKEN                   | -                      | &#10003;* | Get it [here](https://anilist.co/api/v2/oauth/authorize?client_id=1549&response_type=token)                                                              |
| EMBY_EPISODE_COUNT_PRIORITY | -                      | &#10005;  | If set to True, Emby episode watched count will take priority over AniList (default = False)                                                             |
| SKIP_LIST_UPDATE            | -                      | &#10005;  | If set to True, it will NOT update your AniList which is useful if you want to do a test run to check if everything lines up properly. (default = False) |
| LOG_FAILED_MATCHES          | -                      | &#10005;  | If set to True, failed matches will be written to /embyanisync/failed_matches.txt (default = False)                                                      |
| SETTINGS_FILE               | -                      | &#10005;  | Location of a custom settings.ini for more advanced configuration. Makes all settings above obsolete. See section below for usage.                       |
| INTERVAL                    | 3600                   | &#10005;  | The time in between syncs in seconds                                                                                                                     |

### Custom mappings

In order to provide a [custom_mappings.yaml file](https://github.com/RickDB/EmbyAniSync#custom-anime-mapping), mount the file on your host to `/embyanisync/custom_mappings.yaml` like this:

```
-v /path/to/your/custom_mappings.yaml:/embyanisync/custom_mappings.yaml
```

You can modify the file on the host system anytime and it will be used during the next run. Restarting the container is not necessary.

### Custom settings.ini

If you want to use other Emby login mechanisms, you can use your own settings.ini file by mapping it into the container and setting the environment variable `SETTINGS_FILE` with the path to the file inside the container.

If the settings file is located at `/docker/embyanisync/settings.ini` and you want to place it to `/config/settings.ini`, use the following volume mapping and environment variable:

```
-v '/docker/embyanisync/settings.ini:/config/settings.ini:ro'
-e 'SETTINGS_FILE=/config/settings.ini'
```
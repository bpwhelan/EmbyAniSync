# Emby to AniList Sync (WIP)

I'm really bad at python so do not trust this to be 100%, also might need some work setting it up correctly

Currently just meant for private use. Maybe pending approval for public use.


[//]: # ([![Build Status]&#40;https://travis-ci.com/RickDB/EmbyAniSync.svg?branch=master&#41;]&#40;https://travis-ci.com/RickDB/EmbyAniSync&#41;![Docker]&#40;https://github.com/rickdb/Docker-EmbyAniSync/actions/workflows/docker-publish.yml/badge.svg&#41;)

[//]: # ()
[//]: # ()
[//]: # (![Logo]&#40;logo.png&#41;)

[//]: # ()
[//]: # (If you manage your Anime with Emby this will allow you to sync your libraries to [AniList]&#40;https://anilist.co&#41;  , recommend using Emby with the [HAMA agent]&#40;https://github.com/ZeroQI/Hama.bundle&#41; for best Anime name matches.)

[//]: # ()
[//]: # (Unwatched Anime in Emby will not be synced so only those that have at least one watched episode, updates to AniList are only send with changes so need to worry about messing up watch history.)

[//]: # ()
[//]: # ()
[//]: # (This version is based on my previous project  [EmbyMalSync]&#40;https://github.com/RickDB/EmbyMALSync&#41; which due to MAL closing their API is no longer working, this might change in the future and if it does will resume working on that again as as well.)

[//]: # ()
[//]: # ()
[//]: # (**If you want test it out first without updating your actual AniList entries check out ``Skip list updating for testing `` from the ``Optional features`` section of this readme**)

[//]: # ()
[//]: # (## Setup)

[//]: # ()
[//]: # (### Step 1 - install Python)

[//]: # ()
[//]: # (Make sure you have Python 3.7 or higher installed:)

[//]: # ()
[//]: # ([Python homepage]&#40;https://www.python.org/&#41;)

[//]: # ()
[//]: # ()
[//]: # (### Step 2 - Download project files)

[//]: # ()
[//]: # (Get the latest version using your favorite git client or by downloading the latest release from here:)

[//]: # ()
[//]: # (https://github.com/RickDB/EmbyAniSync/archive/master.zip)

[//]: # ()
[//]: # ()
[//]: # (### Step 3 - Configuration)

[//]: # ()
[//]: # (From the project directory rename `settings.ini.example` to `settings.ini`, open `settings.ini` with your favorite text editor and edit where needed.)

[//]: # ()
[//]: # ()
[//]: # (#### Emby)

[//]: # ()
[//]: # (Only choose one of the authentication methods, MyEmby is the easiest.)

[//]: # ()
[//]: # (##### MyEmby authentication &#40;prefered&#41;)

[//]: # ()
[//]: # (For MyEmby authentication you will need your Emby server name and Emby account login information, for example:)

[//]: # ()
[//]: # (```)

[//]: # ([EMBY])

[//]: # (anime_section = Anime)

[//]: # (authentication_method = myemby)

[//]: # ()
[//]: # (server = Sadala)

[//]: # (myemby_user = Goku)

[//]: # (myemby_password = kamehameha)

[//]: # (```)

[//]: # ()
[//]: # (This completes the MyEmby authentication and **only** if you want to sync against a specific Emby Home user which isn't the admin user follow the below instructions:)

[//]: # ()
[//]: # (For this to work lookup the home username on your Emby server and also fill in your full Emby server URL, for example:)

[//]: # ()
[//]: # (```)

[//]: # ([EMBY])

[//]: # (anime_section = Anime)

[//]: # (authentication_method = myemby)

[//]: # ()
[//]: # (# MyEmby)

[//]: # (server = Sadala)

[//]: # (myemby_user = John # has to be the Emby admin user acount)

[//]: # (myemby_password = Doe)

[//]: # ()
[//]: # (# if you enable home_user_sync it will only sync against that specific Emby home user, it requires the full url of your Emby server just like with the Direct IP method)

[//]: # (# home_username is the actual Emby home username and not their e-mail address, this is also case sensitive)

[//]: # ()
[//]: # (home_user_sync = True)

[//]: # (home_username = Megumin # the home user account you want to sync with and can not be the admin user)

[//]: # (home_server_base_url = http://127.0.0.1:32400)

[//]: # (```)

[//]: # ()
[//]: # (##### Direct Emby authentication &#40;advanced users&#41;)

[//]: # ()
[//]: # (The direct authentication method is for users that don't want to use Emby its online authentication system however is more complex to setup, for this you need to find your token manually:)

[//]: # ()
[//]: # (https://support.emby.tv/articles/204059436-finding-an-authentication-token-x-emby-token/)

[//]: # ()
[//]: # (Afterwards can enter your full Emby site url and above authentication token, for example:)

[//]: # ()
[//]: # (```)

[//]: # ([EMBY])

[//]: # (anime_section = Anime)

[//]: # (authentication_method = direct)

[//]: # ()
[//]: # (base_url = http://192.168.1.234:32400)

[//]: # (token = abcdef123456789)

[//]: # (```)

[//]: # ()
[//]: # (##### Section configuration)

[//]: # ()
[//]: # (In the settings file enter your Emby library / section name containing your Anime, for example:)

[//]: # ()
[//]: # (```)

[//]: # ([EMBY])

[//]: # (anime_section = Anime)

[//]: # (```)

[//]: # ()
[//]: # (Multiple libraries are now supported and you separate them by using the pipeline &#40;"|"&#41; character like so:)

[//]: # ()
[//]: # (```)

[//]: # ([EMBY])

[//]: # (anime_section = Anime|Anime2)

[//]: # (```)

[//]: # ()
[//]: # (#### AniList)

[//]: # ()
[//]: # (For AniList you need get a so called `access_token` which you can retrieve via this link and if not logged in will ask you to do so:)

[//]: # ()
[//]: # (https://anilist.co/api/v2/oauth/authorize?client_id=1549&response_type=token)

[//]: # ()
[//]: # (Make sure to copy the entire key as it is pretty long and paste that in the settings file under 'access_token', no need to enclose it just paste it as-is.)

[//]: # ()
[//]: # (Afterwards make sure to also fill in your AniList username as well which is your actual username not your e-mail address like for example:)

[//]: # ()
[//]: # (```)

[//]: # ([ANILIST])

[//]: # (username = GoblinSlayer)

[//]: # (access_token = iLikeToastyGoblins.)

[//]: # (```)

[//]: # ()
[//]: # (### Step 4 - Install requirements)

[//]: # ()
[//]: # (Install the addtional requirements using the Python package installer &#40;pip&#41; from within the project folder:)

[//]: # ()
[//]: # (`pip install -r requirements.txt`)

[//]: # ()
[//]: # ()
[//]: # (### Step 5 - Start syncing)

[//]: # ()
[//]: # (Now that configuration is finished and requirements have been installed we can finally start the sync script:)

[//]: # ()
[//]: # (`python EmbyAniSync.py`)

[//]: # ()
[//]: # (Depending on library size and server can take a few minutes to finish, for scheduled syncing you can create a cronjob, systemd timer or windows task which runs it every 30 minutes for instance.)

[//]: # ()
[//]: # (See [Systemd service]&#40;https://github.com/RickDB/EmbyAniSync/wiki/Systemd-service&#41; for a tutorial on how to set up a timer with systemd.)

[//]: # ()
[//]: # (## Optional features)

[//]: # ()
[//]: # (### Custom anime mapping)

[//]: # ()
[//]: # (You can manually link a Emby title and season to an AniList ID, to do so:)

[//]: # ()
[//]: # (- From the project folder copy `custom_mappings.yaml.example` to `custom_mappings.yaml`)

[//]: # (- Add new entries there in the following format:)

[//]: # ()
[//]: # (```yaml)

[//]: # (  - title: "Emby title for series")

[//]: # (    seasons:)

[//]: # (      - season: Emby season)

[//]: # (        anilist-id: AniList series ID)

[//]: # (      - season: Emby season)

[//]: # (        anilist-id: AniList series ID)

[//]: # (```)

[//]: # ()
[//]: # (If the Emby season should be split into 2 seasons, add an optional `start` parameter to each season like this:)

[//]: # ()
[//]: # (```yaml)

[//]: # (  - title: "Re:ZERO -Starting Life in Another World-")

[//]: # (    seasons:)

[//]: # (      - season: 2)

[//]: # (        anilist-id: 108632)

[//]: # (        start: 1)

[//]: # (      - season: 2)

[//]: # (        anilist-id: 119661)

[//]: # (        start: 14)

[//]: # (```)

[//]: # ()
[//]: # (Episodes 1-13 will be mapped to Re:Zero 2nd Season Part 1, episodes 14 and higher will be mapped to Re:Zero 2nd Season Part 2.)

[//]: # ()
[//]: # (- To find out the AniList ID you can visit the series page and copy it from the site url, like for example My Shield hero has ID 99263:)

[//]: # ()
[//]: # (https://anilist.co/anime/99263/Tate-no-Yuusha-no-Nariagari)

[//]: # ()
[//]: # (- You can remove any existing entries from the example file as they are purely instructional)

[//]: # (- Upon startup it will check if the file is a valid YAML file. The most likely reason it's not is because you didn't put quotes around an anime title with special characters &#40;e.g. ":"&#41; in it.)

[//]: # ()
[//]: # (#### Community mappings)

[//]: # ()
[//]: # (There are some mappings provided by the Github community at https://github.com/RickDB/EmbyAniSync-Custom-Mappings/. For now you can use the mapping files by copying parts into your own mapping file.)

[//]: # ()
[//]: # (The feature of synonyms was introduced for the community mappings where you can specify that a show can have one of multiple titles but should be mapped the same way. See Shaman King &#40;2021&#41; in the example mapping file.)

[//]: # ()
[//]: # (### Custom settings file location)

[//]: # ()
[//]: # (If you want to load a different settings.in file you can do so by supplying it in the first argument like so:)

[//]: # ()
[//]: # (`python EmbyAniSync.py settings_alternate.ini`)

[//]: # ()
[//]: # (In case of the Tautulli sync helper script you can do as well, first argument will then be settings filename and second will be the series name like so:)

[//]: # ()
[//]: # (`python TautulliSyncHelper.py  settings_alternate.ini <emby show name>`)

[//]: # ()
[//]: # (### Make Emby watched episode count take priority)

[//]: # ()
[//]: # (By default if AniList episode count watched is higher than that of Emby it will skip over, this can be overriden with the setting `emby_episode_count_priority`)

[//]: # ()
[//]: # (When set to True it will update the AniList entry if Emby watched episode count is higher than 0 and will not take into account the AniList watched episode count even if that is higher.)

[//]: # ()
[//]: # (**Use this with caution as normally this isn't required and only meant for certain use cases.**)

[//]: # ()
[//]: # (### Skip list updating for testing)

[//]: # ()
[//]: # (In your settings file there's a setting called `skip_list_update` which you can set to True or False, if set to True it will **NOT** update your AniList which is useful if you want to do a test run to check if everything lines up properly.)

[//]: # ()
[//]: # (### Tautulli Sync Helper script)

[//]: # ()
[//]: # (In the project folder you will find `TautulliSyncHelper.py` which you can use to sync a single Emby show to AniList for use in Tautulli script notifcations &#40;trigger on playback stop&#41;.)

[//]: # ()
[//]: # (Usage is as follows:)

[//]: # ()
[//]: # (`python TautulliSyncHelper.py <emby show name>`)

[//]: # ()
[//]: # (Depending on your OS make sure to place the show name between single or double quotes, for more information see the wiki page:)

[//]: # ()
[//]: # (https://github.com/RickDB/EmbyAniSync/wiki/Tautulli-sync-script)

[//]: # ()
[//]: # (## Docker)

[//]: # ()
[//]: # (Docker version is located here: [EmbyAniSync]&#40;https://github.com/RickDB/EmbyAniSync/pkgs/container/embyanisync&#41;)

[//]: # ()
[//]: # (Another docker container for Tautulli with built-in EmbyAniSync can be found here: [Tautulli-EmbyAniSync]&#40;https://github.com/RickDB/EmbyAniSync/pkgs/container/tautulli-embyanisync&#41;)

[//]: # ()
[//]: # ()
[//]: # (## Requirements)

[//]: # ()
[//]: # ([Python 3.7 or higher]&#40;https://www.python.org/&#41;)

[//]: # ()
[//]: # (## Support)

[//]: # ()
[//]: # (Support thread is located on AniList:)

[//]: # ()
[//]: # (https://anilist.co/forum/thread/6443)

[//]: # ()
[//]: # (Optionally also on Emby forums but less active there:)

[//]: # ()
[//]: # (https://forums.emby.tv/t/embyanisync-sync-your-emby-library-to-anilist/365826)

[//]: # ()
[//]: # (## Planned)

[//]: # ()
[//]: # (Currently planned for future releases:)

[//]: # ()
[//]: # (- [ ] XREF title matching based on HAMA which uses custom lists and AniDB)

[//]: # (- [ ] Add setting to skip updating shows with dropped state on user list)

[//]: # (- [ ] Ignore anime list support &#40;based on content rating and / or title&#41;)

[//]: # (- [ ] Improve error handling)

[//]: # ()
[//]: # (## Credits)

[//]: # ()
[//]: # ([Python-EmbyAPI]&#40;https://github.com/pkkid/python-embyapi&#41;)

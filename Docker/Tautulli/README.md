# Docker-Tautulli-EmbyAniSync

A combination of [Tautulli](https://github.com/Tautulli/Tautulli) and EmbyAniSync.

## Usage

### Docker Command

```
docker run -d \
  --name=tautulli-embyanisync \
  -e TZ=<timezone> \
  -e EMBY_SECTION=Anime \
  -e EMBY_URL=http://127.0.0.1:32400 \
  -e EMBY_TOKEN=<embytoken> \
  -e ANI_USERNAME=<anilist-user> \
  -e ANI_TOKEN=<anilist-token> \
  -p 8181:8181 \
  -v <path to tautulli data directory>:/config \
  -v <path to custom_mappings.yaml>:/embyanisync/custom_mappings.yaml \
  --restart unless-stopped \
  ghcr.io/rickdb/tautulli-embyanisync
```

### Environment Variables

Since this is a combination of docker images, environment variables of both images have to be configured.

See:

- [Tautulli](https://github.com/Tautulli/Tautulli-Wiki/wiki/Installation#docker)
- [EmbyAniSync](https://github.com/RickDB/EmbyAniSync/Docker/EmbyAniSync/README.md#environment-variables)

### Configure Tautulli to use EmbyAniSync

After starting the container, Tautulli will be available on the configured port. The default port is 8181.

If you have never configured Tautulli, a setup guide will ask you to set up the connection to the Emby server.

Once the guide is done, follow the instructions [here](https://github.com/RickDB/EmbyAniSync/wiki/Tautulli-sync-script) to set up the EmbyAniSync notification agent.

Use `/embyanisync` as script folder. Do NOT rename TautulliSyncHelper.py to .pyw, otherwise Tautulli won't be able to start it.

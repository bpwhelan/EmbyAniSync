# coding=utf-8
import collections
import json
import logging
import time
from typing import Any, Dict

import requests

logger = logging.getLogger("EmbyAniSync")


# ANILIST_ACCESS_TOKEN = ""
ANILIST_SKIP_UPDATE = False


def search_by_id(anilist_id: int, token: str):
    """Search AniList for a single anime by its media ID.

    Args:
        anilist_id: The AniList media ID.
        token: The AniList API bearer token.

    Returns:
        Parsed JSON response as nested namedtuples.
    """
    query = """
        query ($id: Int) {
        media: Media (id: $id, type: ANIME) {
            id
            type
            format
            status
            source
            season
            episodes
            title {
                romaji
                english
                native
            }
            synonyms
            startDate {
                year
            }
            endDate {
                year
            }
        }
        }
        """

    variables = {"id": anilist_id}

    response = send_graphql_request(query, variables, token)
    return json.loads(response.content, object_hook=to_object)


def search_by_name(anilist_show_name: str, token: str):
    """Search AniList for anime matching a title string (paginated, up to 50 results).

    Args:
        anilist_show_name: The anime title to search for.
        token: The AniList API bearer token.

    Returns:
        Parsed JSON response as nested namedtuples containing page info and media list.
    """
    query = """
        query ($page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                pageInfo {
                    total
                    currentPage
                    lastPage
                    hasNextPage
                    perPage
                }
                media (search: $search, type: ANIME) {
                    id
                    type
                    format
                    status
                    source
                    season
                    episodes
                    title {
                        romaji
                        english
                        native
                    }
                    synonyms
                    startDate {
                        year
                    }
                    endDate {
                        year
                    }
                }
            }
        }
        """
    variables = {"search": anilist_show_name, "page": 1, "perPage": 50}

    response = send_graphql_request(query, variables, token)
    return json.loads(response.content, object_hook=to_object)


def fetch_user_list(username: str, token: str):
    """Fetch a user's complete anime list from AniList.

    Args:
        username: The AniList username.
        token: The AniList API bearer token.

    Returns:
        Parsed JSON response containing MediaListCollection with all lists and entries.
    """
    query = """
        query ($username: String) {
            MediaListCollection(userName: $username, type: ANIME) {
                lists {
                    name
                    status
                    isCustomList
                    entries {
                        id
                        progress
                        status
                        repeat
                        media {
                            id
                            type
                            format
                            status
                            source
                            season
                            episodes
                            startDate {
                                year
                            }
                            endDate {
                                year
                            }
                            title {
                                romaji
                                english
                                native
                            }
                            synonyms
                        }
                    }
                }
            }
        }
        """

    variables = {"username": username}

    response = send_graphql_request(query, variables, token)
    # print(response.content)
    return json.loads(response.content, object_hook=to_object)


def update_series(media_id: int, progress: int, status: str, token: str):
    """Update an anime's watch progress and status on AniList.

    Skips the update if ANILIST_SKIP_UPDATE is enabled.

    Args:
        media_id: The AniList media ID to update.
        progress: The new episode progress count.
        status: The new list status (CURRENT, COMPLETED, etc.).
        token: The AniList API bearer token.
    """
    if ANILIST_SKIP_UPDATE:
        logger.warning(f"[ANILIST] Skip update for {media_id} is enabled in settings so not updating this item")
        return
    query = """
        mutation ($mediaId: Int, $status: MediaListStatus, $progress: Int) {
            SaveMediaListEntry (mediaId: $mediaId, status: $status, progress: $progress) {
                id
                status,
                progress
            }
        }
        """

    variables = {"mediaId": media_id, "status": status, "progress": int(progress)}

    send_graphql_request(query, variables, token)


def send_graphql_request(query: str, variables: Dict[str, Any], token):
    """Send a GraphQL request to the AniList API with rate-limit handling.

    Retries automatically on HTTP 429 responses, and adds a 200ms delay
    between requests to avoid overloading the API.

    Args:
        query: The GraphQL query or mutation string.
        variables: A dict of GraphQL variables.
        token: The AniList API bearer token.

    Returns:
        The requests.Response object.

    Raises:
        requests.HTTPError: If the response has a non-2xx/non-429 status.
    """
    url = "https://graphql.anilist.co"
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    while True:
        response = requests.post(
            url, headers=headers, json={"query": query, "variables": variables}
        )
        if response.status_code == 429:
            wait_time = int(response.headers.get('retry-after', 0))
            logger.warning(f"[ANILIST] Rate limit hit, waiting for {wait_time}s")
            time.sleep(wait_time + 1)

        else:
            response.raise_for_status()

            # wait a bit to not overload AniList API
            time.sleep(0.20)
            return response


def to_object(obj):
    """JSON object_hook that converts dicts to namedtuples for attribute-style access.

    Args:
        obj: A dict from json.loads.

    Returns:
        A namedtuple with keys as attributes.
    """
    keys, values = zip(*obj.items())
    # print(keys, values)
    return collections.namedtuple("X", keys)(*values)

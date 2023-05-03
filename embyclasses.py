from dataclasses import dataclass
from typing import List, Optional

from embypython import BaseItemDto, ProviderIdDictionary, UserItemDataDto
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Show:
    id: int
    anilistID: int
    title: str


@dataclass_json
@dataclass
class UserData:
    played_percentage: float
    unplayed_count: int = 0
    play_count: int = 0
    played: bool = False

    def __init__(self, user_data: UserItemDataDto):
        self.played_percentage = user_data.played_percentage
        self.unplayed_count = user_data.unplayed_item_count or 0
        self.play_count = user_data.play_count or 0
        self.played = user_data.played


@dataclass_json
@dataclass
class ProviderID:
    anilist: str
    tvdb: str
    imdb: str
    tmdb: str

    def __init__(self, provider_ids: ProviderIdDictionary):
        self.anilist = provider_ids.get('AniList')
        self.tvdb = provider_ids.get("Tvdb")
        self.imdb = provider_ids.get("Imdb")
        self.tmdb = provider_ids.get("Tmdb")


@dataclass_json
@dataclass
class EmbySeason:
    id: str
    name: str
    sort_name: str
    series_id: str
    provider_ids: ProviderID
    user_data: UserData
    season_number: int
    episodes_available: int
    episodes_played: int
    year: int

    def __init__(self, item: BaseItemDto):
        self.name = item.name
        self.sort_name = item.sort_name
        self.id = item.id
        self.series_id = item.series_id
        self.provider_ids = ProviderID(item.provider_ids)
        self.type = item.type
        self.user_data = UserData(item.user_data)
        self.season_number = item.index_number
        self.anilist_id = self.provider_ids.anilist
        self.episodes_available = item.recursive_item_count
        self.episodes_played = self.episodes_available - self.user_data.unplayed_count
        self.year = item.production_year


@dataclass_json
@dataclass
class EmbyWatchedSeries:
    title: str
    title_sort: str
    title_original: str
    year: int
    seasons: List[EmbySeason]
    anilist_id: Optional[str]


@dataclass_json
@dataclass
class EmbyShow:
    name: str
    sort_name: str
    id: str
    provider_ids: ProviderID
    type: str
    user_data: UserData
    anilist_id: str
    seasons: List[EmbySeason]
    year: int
    episodes_available: int = 0
    episodes_played: int = 0

    def __init__(self, item: BaseItemDto):
        self.name = item.name
        self.sort_name = item.sort_name
        self.id = item.id
        self.provider_ids = ProviderID(item.provider_ids)
        self.type = item.type
        self.user_data = UserData(item.user_data)
        self.anilist_id = self.provider_ids.anilist
        self.episodes_available = item.recursive_item_count
        # if self.episodes_available is not None:
        self.episodes_played = self.episodes_available - self.user_data.unplayed_count
        self.seasons = []
        self.year = item.production_year

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Show:
    id: int
    anilistID: int
    title: str


@dataclass
class UserData:
    played_percentage: int
    unplayed_count: int
    play_count: int
    played: bool

    def __init__(self, user_data):
        self.played_percentage = user_data.get("PlayedPercentage")
        self.unplayed_count = user_data.get("UnplayedItemCount", 0)
        self.play_count = user_data.get("PlayCount", 0)
        self.played = user_data.get("Played")


@dataclass
class ProviderID:
    anilist: str
    tvdb: str
    imdb: str
    tmdb: str

    def __init__(self, provider_ids):
        self.anilist = provider_ids.get('AniList')
        self.tvdb = provider_ids.get("Tvdb")
        self.imdb = provider_ids.get("Imdb")
        self.tmdb = provider_ids.get("Tmdb")


@dataclass
class EmbySeason:
    id: str
    name: str
    sort_name: str
    series_id: str
    parent_name: str
    provider_ids: List[ProviderID]
    user_data: UserData
    season_number: int
    episodes_available: int
    episodes_played: int
    year: int

    def __init__(self, item):
        self.name = item.get("Name")
        self.sort_name = item.get("SortName")
        self.id = item.get("Id")
        self.series_id = item.get("SeriesId")
        self.provider_ids = ProviderID(item.get("ProviderIds"))
        self.type = item.get("Type")
        self.user_data = UserData(item.get("UserData"))
        self.season_number = item.get("IndexNumber")
        self.anilist_id = self.provider_ids.anilist
        self.episodes_available = item.get("RecursiveItemCount")
        self.episodes_played = self.episodes_available - self.user_data.unplayed_count
        self.year = item.get("ProductionYear")


@dataclass
class EmbyWatchedSeries:
    title: str
    title_sort: str
    title_original: str
    year: int
    seasons: List[EmbySeason]
    anilist_id: Optional[int]


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

    def __init__(self, item):
        print(item)
        self.name = item.get("Name")
        self.sort_name = item.get("SortName")
        self.id = item.get("Id")
        self.provider_ids = ProviderID(item.get("ProviderIds"))
        self.type = item.get("Type")
        self.user_data = UserData(item.get("UserData"))
        self.anilist_id = self.provider_ids.anilist
        self.episodes_available = item.get("RecursiveItemCount", 0)
        # if self.episodes_available is not None:
        self.episodes_played = self.episodes_available - self.user_data.unplayed_count
        self.seasons = []
        self.year = item.get("ProductionYear")

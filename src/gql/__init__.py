# src/gql/__init__.py
from importlib import resources


def _load(name: str) -> str:
    """Helper to load .graphql files from this package."""
    return resources.files(__package__).joinpath(name).read_text()


# ─── Albums ────────────────────────────────────────────────
GET_ALBUM = _load("get_album.graphql")
UPDATE_ALBUM = _load("update_album.graphql")
DELETE_ALBUM = _load("delete_album.graphql")
PAGINATED_ALBUMS = _load("paginated_albums.graphql")
SEARCH_ALBUMS = _load("search_albums.graphql")

# ─── Tracks ────────────────────────────────────────────────
GET_TRACK = _load("get_track.graphql")
UPDATE_TRACK = _load("update_track.graphql")
DELETE_TRACK = _load("delete_track.graphql")
PAGINATED_TRACKS = _load("paginated_tracks.graphql")
SEARCH_TRACKS = _load("search_tracks.graphql")
TRACKS_BY_GENRE = _load("tracks_by_genre.graphql")

# ─── Files ─────────────────────────────────────────────────
FILES = _load("files.graphql")
GET_FILE = _load("get_file.graphql")
UPDATE_FILE = _load("update_file.graphql")
DELETE_FILE = _load("delete_file.graphql")
PAGINATED_FILES = _load("paginated_files.graphql")
SEARCH_FILES = _load("search_files.graphql")

# ─── Genres ────────────────────────────────────────────────
GET_GENRE = _load("get_genre.graphql")
UPDATE_GENRE = _load("update_genre.graphql")
DELETE_GENRE = _load("delete_genre.graphql")
PAGINATED_GENRES = _load("paginated_genres.graphql")

# ─── Labels ────────────────────────────────────────────────
GET_LABEL = _load("get_label.graphql")
UPDATE_LABEL = _load("update_label.graphql")
DELETE_LABEL = _load("delete_label.graphql")
PAGINATED_LABELS = _load("paginated_labels.graphql")

# ─── Persons ───────────────────────────────────────────────
GET_PERSON = _load("get_person.graphql")
UPDATE_PERSON = _load("update_person.graphql")
DELETE_PERSON = _load("delete_person.graphql")
PAGINATED_PERSONS = _load("paginated_persons.graphql")

# ─── Users ─────────────────────────────────────────────────
GET_USER = _load("get_user.graphql")
UPDATE_USER = _load("update_user.graphql")
DELETE_USER = _load("delete_user.graphql")
PAGINATED_USERS = _load("paginated_users.graphql")
SEARCH_USERS = _load("search_users.graphql")

# ─── Tasks & Stats ─────────────────────────────────────────
TASKS = _load("tasks.graphql")
DISPLAY_TASKS = _load("display_tasks.graphql")
STATS = _load("stats.graphql")
TASK_STATS = _load("task_stats.graphql")
TASK_STAT_SUMMARY = _load("task_stat_summary.graphql")
TASK_STAT_TREND = _load("task_stat_trend.graphql")

# ─── Player ────────────────────────────────────────────────
GET_PLAYER_STATUS = _load("get_player_status.graphql")
GET_PLAYER_QUEUE = _load("get_player_queue.graphql")
PLAYER_STATUS = _load("player_status.graphql")
PLAYER_STATUS_SUBSCRIPTION = _load("player_status_subscription.graphql")
QUEUE_TRACK = _load("queue_track.graphql")
PLAY_NEXT = _load("play_next.graphql")
PAUSE = _load("pause.graphql")
STOP = _load("stop.graphql")
SET_POSITION = _load("set_position.graphql")

# ─── Auth ──────────────────────────────────────────────────
LOGIN = _load("login.graphql")
REFRESH = _load("refresh.graphql")
ME = _load("me.graphql")

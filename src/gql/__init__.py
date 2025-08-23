from pathlib import Path


# Helper to resolve query paths
def gql_path(file: str) -> str:
    """Resolves the absolute path to a GraphQL query file within the current package.

    This function constructs the full path to a given GraphQL file name, relative to the directory of this module.

    Args:
        file: The name of the GraphQL file.

    Returns:
        The absolute path to the specified GraphQL file as a string.
    """
    return str(Path(__file__).parent / file)


# Authentication
LOGIN = gql_path("login.graphql")
REFRESH = gql_path("refresh.graphql")
ME = gql_path("me.graphql")

# Tracks
GET_TRACK = gql_path("get_track.graphql")
SEARCH_TRACKS = gql_path("search_tracks.graphql")
UPDATE_TRACK = gql_path("update_track.graphql")
DELETE_TRACK = gql_path("delete_track.graphql")
PAGINATED_TRACKS = gql_path("paginated_tracks.graphql")
TRACKS_BY_GENRE = gql_path("tracks_by_genre.graphql")

# Albums
GET_ALBUM = gql_path("get_album.graphql")
SEARCH_ALBUMS = gql_path("search_albums.graphql")
UPDATE_ALBUM = gql_path("update_album.graphql")
DELETE_ALBUM = gql_path("delete_album.graphql")
PAGINATED_ALBUMS = gql_path("paginated_albums.graphql")

# Genres
GET_GENRE = gql_path("get_genre.graphql")
UPDATE_GENRE = gql_path("update_genre.graphql")
DELETE_GENRE = gql_path("delete_genre.graphql")
PAGINATED_GENRES = gql_path("paginated_genres.graphql")

# Labels
GET_LABEL = gql_path("get_label.graphql")
UPDATE_LABEL = gql_path("update_label.graphql")
DELETE_LABEL = gql_path("delete_label.graphql")
PAGINATED_LABELS = gql_path("paginated_labels.graphql")

# Persons
GET_PERSON = gql_path("get_person.graphql")
UPDATE_PERSON = gql_path("update_person.graphql")
DELETE_PERSON = gql_path("delete_person.graphql")
PAGINATED_PERSONS = gql_path("paginated_persons.graphql")

# Files
FILES = gql_path("files.graphql")
GET_FILE = gql_path("get_file.graphql")
UPDATE_FILE = gql_path("update_file.graphql")
DELETE_FILE = gql_path("delete_file.graphql")
PAGINATED_FILES = gql_path("paginated_files.graphql")

# Tasks & Stats
TASKS = gql_path("tasks.graphql")
DISPLAY_TASKS = gql_path("display_tasks.graphql")
TASK_STATS = gql_path("task_stats.graphql")
TASK_STAT_TREND = gql_path("task_stat_trend.graphql")
STATS = gql_path("stats.graphql")
TASK_STAT_SUMMARY = gql_path("task_stat_summary.graphql")

# Player
GET_PLAYER_QUEUE = gql_path("get_player_queue.graphql")
GET_PLAYER_STATUS = gql_path("get_player_status.graphql")
PLAYER_STATUS = gql_path("player_status.graphql")
PLAYER_STATUS_SUBSCRIPTION = gql_path("player_status_subscription.graphql")
GET_PLAYLIST = gql_path("get_playlist.graphql")

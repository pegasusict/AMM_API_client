# import pytest
from models import PlaybackState, PlayerQueue, PlayerTrack


def test_playertrack_init():
    track = PlayerTrack(
        id=1,
        title="Song A",
        artists=["Artist A"],
        album_picture="cover.jpg",
        duration_seconds=180,
    )
    assert track.id == 1
    assert track.title == "Song A"
    assert track.artists == ["Artist A"]
    assert track.album_picture == "cover.jpg"
    assert track.duration_seconds == 180


def test_playerqueue_init():
    track1 = PlayerTrack(id=1, title="Track 1", artists=["A"], album_picture=None, duration_seconds=100)
    track2 = PlayerTrack(id=2, title="Track 2", artists=["B"], album_picture=None, duration_seconds=200)

    queue = PlayerQueue(tracks=[track1, track2])
    assert len(queue.tracks) == 2
    assert queue.tracks[0].title == "Track 1"
    assert queue.tracks[1].duration_seconds == 200


def test_playbackstate_with_current_track():
    track = PlayerTrack(id=1, title="Now Playing", artists=["Artist"], album_picture=None, duration_seconds=120)

    state = PlaybackState(current_track=track, is_playing=True)  # type: ignore
    assert state.is_playing
    assert state.current_track.title == "Now Playing"  # type: ignore
    assert state.current_track.duration_seconds == 120  # type: ignore


def test_playbackstate_without_current_track():
    state = PlaybackState(current_track=None, is_playing=False)
    assert state.is_playing is False
    assert state.current_track is None

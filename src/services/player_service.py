# services/player_service.py
from typing import AsyncGenerator
from models import PlaybackState, PlaybackTrack
from . import BaseService
from gql import (
    PLAYER_STATUS,
    GET_PLAYER_QUEUE,
    QUEUE_TRACK,
    PLAY_NEXT,
    PAUSE,
    STOP,
    SET_POSITION,
    PLAYER_STATUS_SUBSCRIPTION,
)


class PlayerService(BaseService):
    """Service for controlling and monitoring the player."""

    # Queries
    async def get_status(self) -> PlaybackState:
        """Fetch the current player status."""
        result = await self._exec("get_status", PLAYER_STATUS)
        return PlaybackState(**result["playerStatus"])

    async def get_queue(self) -> list[PlaybackTrack]:
        """Fetch the current player queue as a list of tracks."""
        result = await self._exec("get_queue", GET_PLAYER_QUEUE)
        return [PlaybackTrack(**item) for item in result["playerQueue"]]

    # Mutations
    async def queue_track(self, track_id: int) -> bool:
        result = await self._exec("queue_track", QUEUE_TRACK, {"trackId": track_id})
        return result["queueTrack"]

    async def play_next(self) -> bool:
        result = await self._exec("play_next", PLAY_NEXT)
        return result["playNext"]

    async def pause(self) -> bool:
        result = await self._exec("pause", PAUSE)
        return result["pause"]

    async def stop(self) -> bool:
        result = await self._exec("stop", STOP)
        return result["stop"]

    async def set_position(self, seconds: int) -> bool:
        result = await self._exec("set_position", SET_POSITION, {"seconds": seconds})
        return result["setPosition"]

    # Subscription
    async def subscribe_status(self) -> AsyncGenerator[PlaybackState, None]:
        """Subscribe to live player status updates."""
        async for event in self._subscribe("player_status_subscription", PLAYER_STATUS_SUBSCRIPTION):
            yield PlaybackState(**event["playerStatus"])

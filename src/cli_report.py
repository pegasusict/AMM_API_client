import asyncio
from amm_client import AMMClient


async def list_all_tracks():
    client = AMMClient("http://localhost:8000", persist=True)
    tracks = await client.track.get_tracks_paginated(limit=100, offset=0)
    print(f"Fetched {len(tracks)} tracks:")
    for t in tracks:
        print(f"- {t.title}")


async def list_all_albums():
    client = AMMClient("http://localhost:8000", persist=True)
    albums = await client.album.get_paginated(limit=100, offset=0)
    for a in albums:
        print(f"[{a.releasedate}] {a.title}")


if __name__ == "__main__":
    asyncio.run(list_all_tracks())

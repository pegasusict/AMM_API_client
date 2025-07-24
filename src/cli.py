import asyncio
from amm_client import AMMClient

BASE_URL = "http://localhost:8000"  # or your deployed API


async def main():
    client = AMMClient(BASE_URL)

    print("=== AMM Client Shell ===")
    while True:
        cmd = input("amm> ").strip()
        if cmd in ("exit", "quit"):
            break

        elif cmd.startswith("login"):
            _, email, password = cmd.split()
            await client.login(email, password)
            print("Logged in.")

        elif cmd == "me":
            me = await client.user.get_me()
            print(me)

        elif cmd == "tracks":
            tracks = await client.track.get_tracks(limit=5)
            for t in tracks:
                print(f"- {t.title} [{t.duration}s]")

        elif cmd.startswith("stream"):
            _, user_id = cmd.split()
            print("Stream URL:", client.stream.get_stream_url(user_id))

        else:
            print("Commands: login <email> <pw> | me | tracks | stream <user_id> | exit")


if __name__ == "__main__":
    asyncio.run(main())

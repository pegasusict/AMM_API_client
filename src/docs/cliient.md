
# AMM Python Client SDK

The `AMMClient` provides a typed, async-friendly interface to interact with your music management backend via GraphQL.

---

## 🚀 Quickstart

```python
from amm_client import AMMClient

client = AMMClient("http://localhost:8000")

await client.login("you@example.com", "password")

tracks = await client.track.get_tracks(limit=5)
```

---

## 🧱 Services

### `TrackService`

```python
await client.track.get_tracks()
await client.track.get_tracks_paginated(limit=20, offset=0)
await client.track.search_tracks("Beethoven")
await client.track.get_tracks_by_genre(genre_id=12)
```

### `AlbumService`

```python
await client.album.get_paginated(limit=50)
await client.album.search("Chopin")
```

### `UserService`

```python
user = await client.user.get_me()
status = await client.user.get_playback_state()
```

### `TaskService`

```python
await client.task.get_display_tasks()
await client.task.get_stats()
```

---

## 🔐 Authentication

```python
await client.login("email", "password")
await client.refresh("refresh_token")
```

Tokens are saved automatically if session persistence is enabled (`persist=True`).

---

## 🧪 Testing

```bash
pytest tests/
```

Mocks are used for unit testing. Integration tests run against a local or staging backend.

---

## 🛠 CLI

```bash
amm-client       # Interactive REPL
python cli_report.py  # Predefined reports
```

---

## 📦 Project Layout

```bash
src/
├── gql/
├── services/
├── models/
├── utils/
├── client.py
├── amm_client.py
tests/
docs/
```

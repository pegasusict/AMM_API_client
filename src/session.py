import json
from pathlib import Path


class PersistentSession:
    def __init__(self, filename="~/.amm_client_token.json", enabled=True):
        self.enabled = enabled
        self.path = Path(filename).expanduser()

    def load_token(self) -> str | None:
        if not self.enabled or not self.path.exists():
            return None
        try:
            with self.path.open("r") as f:
                return json.load(f).get("token")
        except Exception:
            return None

    def save_token(self, token: str) -> None:
        if not self.enabled:
            return
        with self.path.open("w") as f:
            json.dump({"token": token}, f)

class StreamService:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_stream_url(self, user_id: str) -> str:
        return f"{self.base_url}/mounts/{user_id}"

    def get_metadata_url(self, user_id: str) -> str:
        return f"{self.base_url}/metadata/{user_id}"

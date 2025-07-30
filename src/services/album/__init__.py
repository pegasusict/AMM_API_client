from .read import AlbumReadService
from .mutate import AlbumMutateService


class AlbumService:
    def __init__(self, gql):
        self.read = AlbumReadService(gql)
        self.mutate = AlbumMutateService(gql)

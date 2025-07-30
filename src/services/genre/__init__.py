from .read import GenreReadService
from .mutate import GenreMutateService


class GenreService:
    def __init__(self, gql):
        self.read = GenreReadService(gql)
        self.mutate = GenreMutateService(gql)

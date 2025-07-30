from .read import TrackReadService
from .mutate import TrackMutateService


class TrackService:
    def __init__(self, gql):
        self.read = TrackReadService(gql)
        self.mutate = TrackMutateService(gql)

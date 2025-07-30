from .read import LabelReadService
from .mutate import LabelMutateService


class LabelService:
    def __init__(self, gql):
        self.read = LabelReadService(gql)
        self.mutate = LabelMutateService(gql)

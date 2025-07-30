from .read import PersonReadService
from .mutate import PersonMutateService


class PersonService:
    def __init__(self, gql):
        self.read = PersonReadService(gql)
        self.mutate = PersonMutateService(gql)

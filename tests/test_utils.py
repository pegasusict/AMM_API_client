# tests/test_utils.py
# import pytest
from errors import GraphQLClientError


def test_graphql_client_error():
    try:
        raise GraphQLClientError("failed", "query", Exception("boom"))
    except GraphQLClientError as e:
        assert "failed" in str(e)
        assert e.operation == "query"

from typing import Optional


class AMMClientError(Exception):
    """Base error for AMM API Client."""


class GraphQLClientError(AMMClientError):
    """Error raised for GraphQL client issues. This includes errors
    related to GraphQL operations, such as query execution failures
    or schema issues."""

    def __init__(self, message: str, operation: Optional[str] = None, original_error: Optional[Exception] = None):
        """
        Initialize a GraphQLClientError.

        Args:
            message (str): Error message.
            operation (Optional[str]): GraphQL operation name.
            original_error (Optional[Exception]): Original error, if any.
        """
        self.operation = operation
        self.original_error = original_error
        super().__init__(f"[{operation}] {message}" if operation else message)

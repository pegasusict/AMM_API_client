from pathlib import Path


def load_query(name: str) -> str:
    """Load a .graphql file from the gql/ directory."""
    query_path = Path(__file__).parent.parent / "gql" / f"{name}.graphql"
    return query_path.read_text(encoding="utf-8")

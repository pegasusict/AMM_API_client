import os
import re
import pytest

# from graphql import parse
from scripts.update_gql_init import update_init

GRAPHQL_DIR = os.path.join(os.path.dirname(__file__), "..", "gql")
INIT_FILE = os.path.join(GRAPHQL_DIR, "__init__.py")


def list_graphql_files():
    return [f for f in os.listdir(GRAPHQL_DIR) if f.endswith(".graphql")]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@pytest.mark.parametrize("filename", list_graphql_files())
def test_graphql_file_valid_syntax(filename):
    """Ensure all GraphQL files parse correctly."""
    from graphql import parse

    source = read_file(os.path.join(GRAPHQL_DIR, filename))
    try:
        parse(source)
    except Exception as e:
        pytest.fail(f"GraphQL syntax error in {filename}: {e}")


@pytest.mark.parametrize("filename", list_graphql_files())
def test_graphql_operation_matches_filename(filename):
    """Ensure operation name matches PascalCase version of filename."""
    source = read_file(os.path.join(GRAPHQL_DIR, filename))
    base = filename.replace(".graphql", "")
    expected = "".join(part.capitalize() for part in base.split("_"))

    match = re.search(r"\b(query|mutation|subscription)\s+(\w+)", source)
    assert match, f"No operation found in {filename}"

    op_name = match[2]
    assert op_name == expected, f"{filename}: expected '{expected}', got '{op_name}'"


def test_all_graphql_files_in_init():
    """Ensure gql/__init__.py matches .graphql files; auto-update if not."""
    files = list_graphql_files()
    init_source = read_file(INIT_FILE)

    missing = []
    # sourcery skip: no-loop-in-tests
    for filename in files:
        const_name = filename.replace(".graphql", "").upper()
        # sourcery skip: no-conditionals-in-tests
        if const_name not in init_source:
            missing.append(filename)

    # sourcery skip: no-conditionals-in-tests
    if missing:
        # Auto-update init file
        update_init()
        pytest.fail(f"Updated gql/__init__.py because these files were missing: {missing}. Re-run tests.")

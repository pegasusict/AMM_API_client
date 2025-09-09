import os
import re
import pytest

SERVICES_DIR = os.path.join(os.path.dirname(__file__), "..", "services")
GQL_INIT = os.path.join(os.path.dirname(__file__), "..", "gql", "__init__.py")

# Load all constants defined in gql/__init__.py
with open(GQL_INIT, "r", encoding="utf-8") as f:
    GQL_INIT_CONTENT = f.read()

CONSTANT_PATTERN = re.compile(r"^([A-Z0-9_]+)\s*=", re.MULTILINE)
GQL_CONSTANTS = set(CONSTANT_PATTERN.findall(GQL_INIT_CONTENT))


def service_files():
    """Yield all Python service files."""
    for root, _, files in os.walk(SERVICES_DIR):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                yield os.path.join(root, file)


@pytest.mark.parametrize("service_file", list(service_files()))
def test_services_use_gql_constants(service_file):
    """Ensure services use gql/__init__.py constants, not raw filenames."""
    with open(service_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for suspicious direct ".graphql" usage
    bad_usages = re.findall(r'"[^"]+\.graphql"|\'[^\']+\.graphql\'', content)
    assert not bad_usages, f"{service_file} hardcodes GraphQL files: {bad_usages}"

    # Ensure at least one known GQL constant is imported if service makes queries
    # sourcery skip: no-conditionals-in-tests
    if "gql import" in content or "from gql" in content:
        used_constants = {c for c in GQL_CONSTANTS if c in content}
        assert used_constants, f"{service_file} imports gql but doesn't use any known constants"

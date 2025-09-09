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


@pytest.mark.parametrize("gql_constant", list(GQL_CONSTANTS))
def test_gql_constants_are_used(gql_constant):
    """Ensure every gql constant is referenced in at least one service."""
    found = False
    # sourcery skip: no-loop-in-tests
    for service_file in service_files():
        with open(service_file, "r", encoding="utf-8") as f:
            content = f.read()
        # sourcery skip: no-conditionals-in-tests
        if gql_constant in content:
            found = True
            break

    assert found, f"GQL constant {gql_constant} is defined in gql/__init__.py but not used in any service"

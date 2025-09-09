# tests/test_service_gql_usage.py
import importlib
import pkgutil
import inspect
import services
from gql import __all__ as gql_constants


def test_services_reference_gql_files():
    gql_names = set(gql_constants)
    unused_services = []

    # sourcery skip: no-loop-in-tests
    for _, module_name, _ in pkgutil.iter_modules(services.__path__):
        # sourcery skip: no-conditionals-in-tests
        if module_name == "__init__":
            continue
        module = importlib.import_module(f"services.{module_name}")
        source = inspect.getsource(module)
        # sourcery skip: no-conditionals-in-tests
        if all(name not in source for name in gql_names):
            unused_services.append(module_name)

    assert not unused_services, f"Services without GraphQL usage: {unused_services}"

# tests/test_models_usage.py
import importlib
import pkgutil
import inspect
import services
import models


def get_all_model_classes():
    model_classes = set()
    for _, module_name, _ in pkgutil.iter_modules(models.__path__):
        if module_name == "__init__":
            continue
        module = importlib.import_module(f"models.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__.startswith("models."):
                model_classes.add(obj)
    return model_classes


def get_all_service_code():
    code = ""
    for _, module_name, _ in pkgutil.iter_modules(services.__path__):
        if module_name == "__init__":
            continue
        module = importlib.import_module(f"services.{module_name}")
        code += inspect.getsource(module)
    return code


def test_all_models_used_in_services():
    model_classes = get_all_model_classes()
    service_code = get_all_service_code()
    unused = []
    unused.extend(cls.__name__ for cls in model_classes if cls.__name__ not in service_code)
    assert not unused, f"Models not referenced in services: {unused}"

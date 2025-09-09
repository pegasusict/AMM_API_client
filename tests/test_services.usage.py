# tests/test_services_usage.py
import os
import glob

SERVICES_DIR = "src/services"
TESTS_DIR = "tests/services"


def test_all_services_have_tests():
    service_files = [os.path.basename(f) for f in glob.glob(f"{SERVICES_DIR}/*.py") if "__init__" not in f]
    test_files = [os.path.basename(f).replace("test_", "") for f in glob.glob(f"{TESTS_DIR}/test_*.py")]

    missing = [s for s in service_files if s not in test_files]
    assert not missing, f"Missing tests for services: {missing}"

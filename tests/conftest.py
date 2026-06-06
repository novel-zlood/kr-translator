import os

import pytest


@pytest.fixture()
def source_test_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "resources", "test_file.txt")


@pytest.fixture()
def sound_test_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "resources", "test_sound_effect.txt")


@pytest.fixture()
def source_text(source_test_file):
    with open(source_test_file, "r") as f:
        return f.read()

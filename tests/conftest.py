import pytest_asyncio
import os


@pytest_asyncio.fixture()
def source_test_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_location = os.path.join(current_dir, "resources", "test_file.txt")

    return file_location


@pytest_asyncio.fixture()
def sound_test_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_location = os.path.join(current_dir, "resources", "test_sound_effect.txt")

    return file_location


@pytest_asyncio.fixture()
def source_text():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_location = os.path.join(current_dir, "resources", "test_file.txt")

    text = open(file_location, "r")

    return text

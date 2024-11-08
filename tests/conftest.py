import pytest
from selenium import webdriver

from config import config


@pytest.fixture
def driver():
    """Gets a new browser from the 'config.py' hand it over to the test and then close it after the test is finished.

    Yields:
        selenium.webdriver: driver to the select browser by config.py
    """
    driver = config.get_webdriver()
    yield driver
    driver.quit()

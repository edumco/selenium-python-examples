import distro
import platform

from enum import Enum
from importlib.metadata import distribution
import installed_browsers

import shutil

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def browser_path(browser_name: str):
    return shutil.which(browser_name)


# Helps the code readability and can be expanded if needed
class MyConfiguration(Enum):
    CHROME_ON_LINUX = 1
    CHROME_ON_LINUX_SNAP = 2
    CHROME_ON_WINDOWS = 3
    FIREFOX_ON_LINUX = 4
    FIREFOX_ON_LINUX_SNAP = 5
    FIREFOX_ON_WINDOWS = 6


def get_my_configuration():

    my_system = platform.system().lower()
    my_distro = distro.name().lower()
    my_browser = installed_browsers.what_is_the_default_browser().lower()

    if my_system == "windows" and my_browser == "firefox":
        return MyConfiguration.FIREFOX_ON_WINDOWS

    if my_system == "windows" and my_browser == "chrome":
        return MyConfiguration.CHROME_ON_WINDOWS

    if my_system == "linux" and my_distro == "ubuntu" and my_browser == "firefox":
        return MyConfiguration.FIREFOX_ON_LINUX_SNAP

    if my_system == "linux" and my_distro == "ubuntu" and my_browser == "chrome":
        return MyConfiguration.CHROME_ON_LINUX_SNAP

    if my_system == "linux" and my_browser == "firefox":
        return MyConfiguration.FIREFOX_ON_LINUX

    if my_system == "linux" and my_browser == "chrome":
        return MyConfiguration.CHROME_ON_LINUX


def get_webdriver():

    my_configuration = get_my_configuration()
    print(my_configuration)

    # TODO ADD all the configurations
    if my_configuration == MyConfiguration.FIREFOX_ON_LINUX_SNAP:

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = (
            "/snap/firefox/current/usr/lib/firefox/firefox"
        )
        firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        return driver

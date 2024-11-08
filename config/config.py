from enum import Enum
from selenium import webdriver

import os
import distro
import platform
import installed_browsers
import shutil

EXPLICIT_WAIT = 15


def chrome_binary():
    if distro.name().lower() == "ubuntu":
        return "/snap/bin/chromium"
    else:
        return shutil.which("google-chrome")


def firefox_binary():
    if distro.name().lower() == "ubuntu":
        return "/snap/firefox/current/usr/lib/firefox/firefox"
    else:
        return shutil.which("firefox")


def get_driver_path(browser: str, os_type: str):

    if browser == "chrome":
        driver_name = "chromedriver"
    elif browser == "firefox":
        driver_name = "geckodriver"
    elif browser == "edge":
        driver_name = "msedgedriver"
    else:
        raise ValueError("Browser not supported")

    if os_type == "windows":
        driver_name += ".exe"

    if os_type == "darwin":
        os_type = "mac_arm"

    base_driver_path = os.path.join(os.path.dirname(__file__), "..", "drivers")

    return os.path.join(base_driver_path, os_type, browser, driver_name)


# TODO Add edge
def my_webdriver():

    my_browser = installed_browsers.what_is_the_default_browser().lower()

    if my_browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = firefox_binary()
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        return driver

    elif my_browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_binary()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver

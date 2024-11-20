from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import os
import distro
import platform
import installed_browsers
import shutil

EXPLICIT_WAIT = 15


def chrome_binary():
    if distro.name().lower() == "ubuntu":
        return "/snap/bin/google-chrome"
    else:
        return shutil.which("google-chrome")


def firefox_binary():
    if distro.name().lower() == "ubuntu":
        return "/snap/firefox/current/usr/lib/firefox/firefox"
    else:
        return shutil.which("firefox")


def get_driver_path(browser: str, os_type: str):

    if browser == "google-chrome":
        driver_name = "chromedriver"
    elif browser == "firefox":
        driver_name = "geckodriver"
    elif browser == "microsoft-edge":
        driver_name = "msedgedriver"
    else:
        raise ValueError("Browser not supported")

    if os_type == "windows":
        driver_name += ".exe"

    if os_type == "darwin":
        os_type = "mac_arm"

    base_driver_path = os.path.join(os.path.dirname(__file__), "..", "drivers")

    return os.path.join(base_driver_path, os_type, browser, driver_name)


def my_webdriver():

    my_browser = (
        installed_browsers.what_is_the_default_browser().lower().replace(" ", "-")
    )

    my_os = platform.system().lower()

    if my_browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = firefox_binary()
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        return driver

    elif my_browser == "google-chrome":

        chrome_binary_path = shutil.which("google-chrome")
        os.environ["PATH"] += os.pathsep + chrome_binary_path

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_binary_path

        driver_path = get_driver_path(my_browser, my_os)
        service = ChromeService(executable_path=driver_path)

        driver = webdriver.Chrome(options=chrome_options, service=service)
        driver.maximize_window()
        return driver

    elif my_browser == "microsoft-edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.binary_location = shutil.which("microsoft-edge")
        driver = webdriver.Chrome(options=edge_options)
        driver.maximize_window()
        return driver

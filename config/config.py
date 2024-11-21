from selenium import webdriver

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ChromeService

from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import FirefoxService


import os
import distro
import platform
import installed_browsers
import shutil


EXPLICIT_WAIT = 15


def my_platform():
    """The os name and architeture: linux64, mac-arm64, macx64 and win64

    Raises:
        ValueError: System is not supported.

    Returns:
        _type_: str
    """
    os_name = platform.system().lower()
    arch = platform.processor()

    if os_name == "darwin":
        if arch == "arm":
            return "mac-arm64"  # apple silicon
        else:
            return "mac-x64"  # old intel

    elif os_name == "windows" and arch == "x86_64":
        return "win64"

    elif os_name == "linux" and arch == "x86_64":
        return "linux64"

    else:
        raise ValueError("System not supported")


def my_browser():

    browser = installed_browsers.what_is_the_default_browser().lower()
    if browser == "google chrome":
        return "chrome"

    return browser


def is_a_valid_browser(browser_name):
    return browser_name in ["chrome", "firefox", "msedge", "safari"]


def my_browsers():
    """List the installed browsers

    Returns:
        _type_: List of browsers information dictionaries
    """
    my_browsers = []

    for browser in installed_browsers.browsers():

        if is_a_valid_browser(browser["name"]):
            my_browsers.append(browser)

    return my_browsers


def select_a_valid_browser():

    default_browser = my_browser()

    if is_a_valid_browser(default_browser):
        return default_browser
    elif len(my_browsers()) > 0:
        return my_browsers()[0]["name"]
    else:
        raise ValueError("No supported browser")


def get_driver_path(browser: str, platform: str):

    if browser == "chrome":
        driver_name = "chromedriver"
    elif browser == "firefox":
        driver_name = "geckodriver"
    elif browser == "msedge":
        driver_name = "msedgedriver"
    else:
        raise ValueError("Browser not supported")

    if platform == "win64":
        driver_name += ".exe"

    if platform == "darwin":
        platform = "mac_arm64"

    base_driver_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "drivers"
    )

    return os.path.join(base_driver_path, platform, browser, driver_name)


def firefox_binary():
    if distro.name().lower() == "ubuntu":
        return "/snap/firefox/current/usr/lib/firefox/firefox"
    else:
        return shutil.which("firefox")


def my_webdriver():

    browser = select_a_valid_browser()
    my_os = my_platform()

    if browser == "firefox":

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.binary_location = firefox_binary()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        return driver

    elif browser == "chrome":

        binary_path = shutil.which("google-chrome")
        os.environ["PATH"] += os.pathsep + binary_path
        options = ChromeOptions()
        options.add_argument("--headless")

        service = ChromeService(executable_path=get_driver_path(browser, my_os))

        driver = Chrome(
            options=options,
            service=service,
        )
        driver.maximize_window()

        return driver

    elif browser == "msedge":
        options = webdriver.EdgeOptions()
        options.binary_location = shutil.which("microsoft-edge")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver = webdriver.Edge(
            options=webdriver.EdgeOptions(), service=webdriver.EdgeService()
        )

        return driver


print(my_platform())
print(my_browser())

print(my_browsers())
print(select_a_valid_browser())
print(get_driver_path(select_a_valid_browser(), my_platform()))

browser = select_a_valid_browser()
version = installed_browsers.get_version_of(browser)["version"]

import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password",
    [("demouser", "abc123")],
)
def test_tc001_login_positive(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.is_authenticated(), "Could not authenticate"


# TODO read invalid users from config or generate random combinations
@pytest.mark.parametrize(
    "username, password",
    [
        ("Demouser", "abc123"),
        ("demouser_", "xyz"),
        ("demouser", "nananana"),
        ("demouser", "abc123"),
    ],
)
def test_tc002_login_negative(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert login_page.is_not_authenticated(), "Wrong authentication"

import pytest
from selenium import webdriver
from pages.login_page import LoginPage


def test_tc001_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.login(username="demouser", password="abc123")
    assert login_page.is_authenticated(), "Could not authenticate"


# @pytest.mark.parametrize(
#     "username, password",
#     [
#         ("Demouser", "abc123"),
#         ("demouser_", "xyz"),
#         ("demouser", "nananana"),
#         ("demouser", "abc123"),  # should fail
#     ],
# )
# def test_tc002_login_negative(driver, username, password):
#     login_page = LoginPage(driver)
#     login_page.login(username, password)
#     assert login_page.element_is_visible(
#         LoginPage.ERROR_ALERT_SELECTORS
#     ), "Doesn't show the correct error message"

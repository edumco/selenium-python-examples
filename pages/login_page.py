from ast import Tuple
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as DriverWait
from selenium.webdriver.support import expected_conditions as Condition


# TODO create a docstring and add the following info:
# * extracts the tuple to the inputs
# The tuples will be used to select the element on page
# TODO extract URL to config


class LoginPage:

    LOGIN_URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"

    USERNAME_SELECTORS = (By.NAME, "username")
    PASSWORD_SELECTORS = (By.NAME, "password")
    LOGIN_BUTTON_SELECTORS = (By.ID, "btnLogin")
    ERROR_MESSAGE_SELECTORS = (By.CSS_SELECTOR, ".alert")
    INVOICE_PAGE_SELECTORS = (By.PARTIAL_LINK_TEXT, "Invoice")

    def __init__(self, webdriver: webdriver):
        self.driver = webdriver
        self.driver.get(self.LOGIN_URL)

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME_SELECTORS)
        ActionChains(self.driver).move_to_element(username_field).send_keys_to_element(
            username_field, *username
        ).perform()

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_SELECTORS)
        password_field.clear()
        password_field.send_keys(password)

    def confirm_form(self):

        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTORS)
        login_button.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.confirm_form()

    # TODO treat exceptions
    # TODO change wait accordinly with the page avg page load
    def is_authenticated(self) -> bool:
        wait = DriverWait(self.driver, 8)
        web_element = wait.until(
            Condition.visibility_of_element_located(LoginPage.INVOICE_PAGE_SELECTORS)
        )
        if web_element.text.__contains__("Invoice"):
            return True
        else:
            return False

    # This inversion makes it run faster on slow networks
    # TODO treat exceptions
    # TODO change wait accordinly with the page avg page load
    def is_not_authenticated(self) -> bool:
        wait = DriverWait(self.driver, 8)
        web_element = wait.until(
            Condition.visibility_of_element_located(LoginPage.ERROR_MESSAGE_SELECTORS)
        )
        if web_element.text.__contains__("Wrong"):
            return True
        else:
            return False

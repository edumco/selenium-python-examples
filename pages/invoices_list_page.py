from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as DriverWait
from selenium.webdriver.support import expected_conditions as Condition


class InvoicesListPage:

    INVOICE_LINKS = (By.LINK_TEXT, "Invoice Details")

    def __init__(self, webdriver: webdriver):
        self.driver = webdriver

    def list_invoices(self) -> list:
        wait = DriverWait(self.driver, 20)
        elements = wait.until(
            Condition.presence_of_all_elements_located(self.INVOICE_LINKS)
        )

        urls = [
            e.get_attribute("href")
            for e in elements
            if e.get_attribute("href") is not None
        ]
        return urls

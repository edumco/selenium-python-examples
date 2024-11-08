import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.invoices_list_page import InvoicesListPage


# TODO read size from config on the running
# TODO read valid user from config
def test_count_invoices(driver):
    login = LoginPage(driver).login("demouser", "abc123")
    if login.is_authenticated():
        invoices = InvoicesListPage(driver)
        urls = invoices.list_invoices()
    assert len(urls) == 2, "Invoice list size not expected"

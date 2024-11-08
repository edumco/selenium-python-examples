import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.invoices_list_page import InvoicesListPage
from pages.invoice_detail_page import InvoiceDetailsPage


# TODO read size from config


def test_count_invoices(logged_driver):
    urls = InvoicesListPage(logged_driver).list_invoices()
    assert len(urls) == 2, "Invoice list size not expected"


def test_tc003_validate_invoice_details(logged_driver):
    first_invoice_url = InvoicesListPage(logged_driver).list_invoices()[0]
    invoice = InvoiceDetailsPage(logged_driver, first_invoice_url)
    invoice_data = invoice.extract_all()
    assert invoice_data != None
    assert len(invoice_data) > 0

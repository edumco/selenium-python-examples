import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.invoices_list_page import InvoicesListPage
from pages.invoice_detail_page import InvoiceDetailsPage


def compare_dicts(expected, found):
    differences = {
        "mismatched_values": {},
        "missing_in_found": {},
        "extra_in_found": {},
    }

    for key in expected:
        if key in found:
            if expected[key] != found[key]:
                differences["mismatched_values"][key] = {
                    "expected": expected[key],
                    "found": found[key],
                }
        else:
            differences["missing_in_found"][key] = expected[key]

    for key in found:
        if key not in expected:
            differences["extra_in_found"][key] = found[key]

    return differences


expected_data = {
    "hotel": "Rendezvous Hotel",
    "invoice_id": "110",
    "invoice_date": "14/01/2018",
    "invoice_due_date": "15/01/2018",
    "Booking Code": "0875",
    "Room": "Superior Double",
    "Total Stay Count": "1",
    "Total Stay Amount": "$150",
    "Check-In": "14/01/2018",
    "Check-Out": "15/01/2018",
    "customer_details": "JOHNY SMITH, R2, AVENUE DU MAROC, 123456",
    "Deposit Nowt": "USD $20.90",  # Typo on page
    "Tax&VAT": "USD $19",
    "Total Amount": "USD $209",
}


def test_tc003_validate_invoice_details(logged_driver):
    invoice_url = InvoicesListPage(logged_driver).list_invoices()[0]
    invoice = InvoiceDetailsPage(logged_driver, invoice_url)
    invoice_data = invoice.extract_all_details()
    assert invoice_data != None, "Can't read invoice data"
    differences = compare_dicts(expected_data, invoice_data)
    mismatch = differences["mismatched_values"]
    missing = differences["missing_in_found"]
    extra = differences["extra_in_found"]
    assert len(mismatch) == 0
    assert len(missing) == 0
    assert len(extra) == 0

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as DriverWait
from selenium.webdriver.support import expected_conditions as Condition


class InvoiceDetailsPage:

    INVOICE_BILLING_SECTION = (By.CSS_SELECTOR, "h5.mt-5:nth-child(11)")

    def __init__(self, webdriver, url: str):
        self.driver = webdriver
        self.url = url
        self.driver.get(url)
        wait = DriverWait(self.driver, 8)  # wait page load
        wait.until(Condition.presence_of_element_located(self.INVOICE_BILLING_SECTION))

    def extract_all_details(self):
        invoice_data = {}
        invoice_data["hotel"] = self._extract_hotel()
        invoice_data["invoice_id"] = self._extract_invoice_id()
        invoice_data["invoice_date"], invoice_data["invoice_due_date"] = (
            self._extract_invoice_dates()
        )
        invoice_data.update(self._extract_booking_details())
        invoice_data.update(self._extract_stay_details())
        invoice_data["customer_details"] = self._extract_customer_details()
        invoice_data.update(self._extract_billing_details())
        return invoice_data

    def _extract_hotel(self):
        hotel = self.driver.find_element(By.CSS_SELECTOR, "h4.mt-5")
        return hotel.text

    def _extract_invoice_id(self):
        invoice_id = self.driver.find_element(By.CSS_SELECTOR, ".mt-2")
        return invoice_id.text.split("#")[1].split(" ")[0]

    def _extract_invoice_dates(self):
        invoice_date = self.driver.find_element(
            By.CSS_SELECTOR, ".container > ul:nth-child(5) > li:nth-child(1)"
        )
        due_date = self.driver.find_element(
            By.CSS_SELECTOR, ".container > ul:nth-child(5) > li:nth-child(2)"
        )
        return (
            invoice_date.text.split(":")[1].strip(),
            due_date.text.split(":")[1].strip(),
        )

    def _extract_booking_details(self):
        booking_data = {}
        booking_table = self.driver.find_element(
            By.CSS_SELECTOR, "table.table:nth-child(8)"
        )
        booking_rows = booking_table.find_elements(By.TAG_NAME, "tr")
        for row in booking_rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) == 2:
                booking_data[columns[0].text] = columns[1].text
        return booking_data

    def _extract_stay_details(self):
        stay_data = {}
        stay_table_rows = self.driver.find_elements(
            By.CSS_SELECTOR, "table:nth-of-type(1) tr"
        )
        for row in stay_table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                stay_data[cells[0].text] = cells[1].text
        return stay_data

    def _extract_customer_details(self):
        customer_details = self.driver.find_element(
            By.CSS_SELECTOR, "html body section.content div.container div"
        )
        return customer_details.text.replace("\n", ", ")

    def _extract_billing_details(self):
        billing_data = {}
        billing_rows = self.driver.find_elements(
            By.CSS_SELECTOR, "table:nth-of-type(2) tr"
        )
        headers = billing_rows[0].find_elements(By.TAG_NAME, "td")
        values = billing_rows[1].find_elements(By.TAG_NAME, "td")
        for header, value in zip(headers, values):
            billing_data[header.text] = value.text
        return billing_data

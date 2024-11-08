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

    def extract_all(self):

        invoice_data = {}

        # Hotel
        hotel = self.driver.find_element(By.CSS_SELECTOR, "h4.mt-5")
        invoice_data["hotel"] = hotel.text

        # Invoice ID
        invoice_id = self.driver.find_element(By.CSS_SELECTOR, ".mt-2")
        invoice_id_text = invoice_id.text.split("#")[1].split(" ")[0]
        invoice_data["invoice_id"] = invoice_id_text

        # Invoice Dates
        invoice_date = self.driver.find_element(
            By.CSS_SELECTOR, ".container > ul:nth-child(5) > li:nth-child(1)"
        )
        date_text = invoice_date.text.split("</span>")[0].split(" ")[2]
        invoice_data["invoice_date"] = date_text

        invoice_due_date = self.driver.find_element(
            By.CSS_SELECTOR,
            ".container > ul:nth-child(5) > li:nth-child(2)",
        )
        due_date_text = invoice_due_date.text.split("</span>")[0].split(" ")[2]
        invoice_data["invoice_due_date"] = due_date_text

        # Booking details
        # table.table:nth-child(8)
        booking_table = self.driver.find_element(
            By.CSS_SELECTOR, "table.table:nth-child(8)"
        )
        booking_rows = booking_table.find_elements(By.TAG_NAME, "tr")
        for row in booking_rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            label = columns[0].text
            value = columns[1].text
            invoice_data[label] = value

        # Table 'Booking/Stay details'
        stay_table_rows = self.driver.find_elements(
            By.CSS_SELECTOR, "table:nth-of-type(1) tr"
        )
        for row in stay_table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                label = cells[0].text
                value = cells[1].text
                invoice_data[label] = value

        # Customer details
        customer_details = self.driver.find_element(
            By.CSS_SELECTOR, "html body section.content div.container div"
        )
        invoice_data["customer_details"] = customer_details.text.replace("\n", ", ")

        # Billing Details
        billing_rows = self.driver.find_elements(
            By.CSS_SELECTOR, "table:nth-of-type(2) tr"
        )
        billing_headers = billing_rows[0].find_elements(By.TAG_NAME, "td")
        billing_values = billing_rows[1].find_elements(By.TAG_NAME, "td")

        for header, value in zip(billing_headers, billing_values):
            invoice_data[header.text] = value.text

        return invoice_data

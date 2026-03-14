from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BookPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.add_to = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '._button_ssd04_1._is-m_ssd04_85._is-blue_ssd04_102._is-expanded_ssd04_98._is-rounded_ssd04_94')))
        self.add_to.click()

    def wait_url_books(self):
        self.wait.until(EC.url_contains("/books/"))

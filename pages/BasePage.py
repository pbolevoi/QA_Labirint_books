from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_cart_counter(self):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '._cartCount_1a3wc_104'), '1'))
        self.counter = self.driver.find_element(
            By.CSS_SELECTOR, '._cartCount_1a3wc_104').text
        return self.counter == '1'

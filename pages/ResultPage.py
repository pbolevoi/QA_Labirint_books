from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ResultPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_book(self, index=0):
        self.books = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.product-card__img')))
        self.books[index].click()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.labirint.ru/')
        self.driver.add_cookie({'name': 'cookie_policy', 'value': '1'})

    def search_field(self):
        self.driver.find_element(
            By.XPATH, '//input[@id="search-field"]').send_keys('python', Keys.ENTER)

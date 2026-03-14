from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.BookPage import BookPage
from pages.BasePage import BasePage

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
options = webdriver.FirefoxOptions()
options.add_argument('--incognito')
options.add_argument('--window-size=1200,800')

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(4)
wait = WebDriverWait(driver, 10)


def test_1():
    main = MainPage(driver)
    main.open()
    main.search_field()

    result = ResultPage(driver)
    result.go_to_book()

    book = BookPage(driver)
    book.wait_url_books()
    book.add_to_cart()

    base = BasePage(driver)
    driver.quit()


# -------------------


def test_2():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.labirint.ru/')
    driver.add_cookie(cookie_dict=cookie)
    driver.find_element(
        By.XPATH, '//input[@id="search-field"]').send_keys('python', Keys.ENTER)

    to_cart = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, '.buy-link')))
    to_cart[0].click()
    books = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.product-card__img')))
    books[0].click()

    plus = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '._plus_htzb6_30')))
    print(plus.is_displayed())
    print(plus.is_enabled())

    driver.quit()


test_1()
test_2()

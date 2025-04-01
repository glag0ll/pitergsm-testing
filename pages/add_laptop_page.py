import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Add_laptop(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    first_price = "//input[contains(@class, 'js_range_from') and contains(@class, 'filter-input__field--from') and @name='arrFilter_P1_MIN']"
    second_price = "//input[contains(@class, 'js_range_to') and contains(@class, 'filter-input__field--to') and @name='arrFilter_P1_MAX']"
    show_laptops = "//button[contains(@class, 'btn_cta') and @for='show-filter' and normalize-space()='Показать товары']"
    buy_laptop = "//button[contains(@class, 'buy_link') and @data-product-id='31947' and .//span[normalize-space()='Купить']]"
    continue_shopping = "//button[contains(@class, 'js_popup_close') and contains(@class, 'btn_outline') and normalize-space()='Продолжить покупки']"

    # getters
    def get_first_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.first_price)))

    def get_second_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.second_price)))

    def get_laptops(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.show_laptops)))

    def buying_laptop(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.buy_laptop)))

    def get_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.continue_shopping)))


    # actions
    def input_first_price(self, first_price):
        self.get_first_price().send_keys(Keys.CONTROL + 'a')
        self.get_first_price().send_keys(Keys.DELETE)
        self.get_first_price().send_keys(first_price)
        print('added first price')

    def input_second_price(self, second_price):
        self.get_second_price().send_keys(Keys.CONTROL + 'a')
        self.get_second_price().send_keys(Keys.DELETE)
        self.get_second_price().send_keys(second_price)
        print('added second price')
        time.sleep(1)

    def click_get_laptops(self):
        self.get_laptops().click()
        print('click')
        time.sleep(1)

    def click_buying_laptop(self):
        self.buying_laptop().click()
        print('click')
        time.sleep(1)

    def click_continue(self):
        self.get_continue().click()
        print('click')

    def add_laptop(self):
        self.get_current_url()
        self.input_first_price('0')
        self.input_second_price('50000')
        self.click_get_laptops()
        self.click_buying_laptop()
        self.click_continue()

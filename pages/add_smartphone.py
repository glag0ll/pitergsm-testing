import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from utilities.logger import Logger


class Add_smartphone(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    smartphones_page = "//a[contains(@class, 'hcat__link') and contains(@class, 'js_hcat-sub-trigger') and @href='/catalog/phones/' and normalize-space(text())='Смартфоны']"
    first_price = "//input[contains(@class, 'js_range_from') and contains(@class, 'filter-input__field--from') and @name='arrFilter_P1_MIN']"
    second_price = "//input[contains(@class, 'js_range_to') and contains(@class, 'filter-input__field--to') and @name='arrFilter_P1_MAX']"
    show_smartphones = "//button[contains(@class, 'btn_cta') and @for='show-filter' and normalize-space()='Показать товары']"
    buy_smartphone = "//button[contains(@class, 'buy_link') and @data-product-id='55029' and .//span[contains(@class, 'prodcard__btn-text') and normalize-space()='Купить']]"
    continue_shopping = "//button[contains(@class, 'js_popup_close') and contains(@class, 'btn_outline') and normalize-space()='Продолжить покупки']"

    # getters
    def get_smartphone_page(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.smartphones_page)))

    def get_first_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.first_price)))

    def get_second_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.second_price)))

    def get_all_smartphones(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.show_smartphones)))

    def buying_smartphone(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.buy_smartphone)))

    def get_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.continue_shopping)))

    # actions
    def click_get_smartphones(self):
        self.get_smartphone_page().click()
        print('переходим на страницу смартфонов')

    def input_first_price(self, first_price):
        self.get_first_price().send_keys(Keys.CONTROL + 'a')
        self.get_first_price().send_keys(Keys.DELETE)
        self.get_first_price().send_keys(first_price)
        print('вставлена первая цена')

    def input_second_price(self, second_price):
        self.get_second_price().send_keys(Keys.CONTROL + 'a')
        self.get_second_price().send_keys(Keys.DELETE)
        self.get_second_price().send_keys(second_price)
        print('вставлена вторая цена')
        time.sleep(1)

    def click_all_smartphones(self):
        self.get_all_smartphones().click()
        print('клик по отсортированным смартфонам')
        time.sleep(1)

    def scroll_to_smartphone(self, smartphone):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", smartphone)

    def click_buying_smartphone(self):
        smartphone = self.buying_smartphone()
        self.scroll_to_smartphone(smartphone)
        smartphone.click()
        print('кнопка добавления смартфона в корзину нажата')

    def click_continue(self):
        self.get_continue().click()
        print('кнопка "продолжить" нажата')

    def add_smartphone(self):
        Logger.add_start_step(method='add_smartphone')
        self.get_current_url()
        self.click_get_smartphones()
        self.input_first_price('20000')
        self.input_second_price('30000')
        self.click_all_smartphones()
        self.click_buying_smartphone()
        time.sleep(1)
        self.get_screen()
        self.click_continue()
        Logger.add_end_step(url=self.driver.current_url, method='add_smartphone')
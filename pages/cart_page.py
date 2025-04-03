from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from base.base import Base

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    place_order = "//a[contains(@class, 'cartplate__btn') and @href='/personal/cart/' and normalize-space()='Оформить']"
    proceed_to_order = "//a[contains(@class, 'btn_cta') and @href='/personal/order/make/' and normalize-space()='Перейти к оформлению']"
    full_name = "//input[@name='ORDER_PROP_1' and contains(@class, 'form__input') and @placeholder='Ф.И.О.']"
    phone = "//input[@name='ORDER_PROP_3' and contains(@class, 'js_mask_phone') and @placeholder='Телефон']"
    commentary = "//textarea[@name='ORDER_DESCRIPTION' and @placeholder='Комментарий']"


    # getters
    def get_place_order(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.place_order)))

    def get_proceed_to_order(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.proceed_to_order)))

    def get_full_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.full_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.phone)))

    def get_commentary(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.commentary)))

    # actions
    def click_place_order(self):
        self.get_place_order().click()
        print('click')

    def click_proceed_to_order(self):
        self.get_proceed_to_order().click()
        print('click')

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print('input full_name')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('input phone')

    def input_commentary(self, commentary):
        self.get_commentary().send_keys(commentary)
        print('input commentary')

    def cart_checkout(self):
        self.click_place_order()
        self.click_proceed_to_order()
        self.input_full_name('Иванов Иван Иванович')
        self.input_phone('+79000000000')
        self.input_commentary('клёвый сайт :)')




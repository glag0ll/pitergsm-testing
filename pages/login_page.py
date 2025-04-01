from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

from base.base import Base


class Login_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    profile_button = '//button[@data-target="#popup_login_by_code"]'
    enter_with_pass = '//button[@id="loginByPassword"]'
    username = "//input[contains(@class, 'form__input') and @name='username']"
    password = '//input[@type="password"]'
    enter_button = "//button[contains(@class, 'btn_cta')][@type='submit'][text()='Войти']"
    main_word = "//h2[contains(@class, 'slider__title') and text()='Популярные товары']"

    # getters
    def get_profile_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_enter_pass(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_with_pass)))

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # actions
    def click_profile_button(self):
        self.get_profile_button().click()
        print('click')

    def click_enter_with_pass(self):
        self.get_enter_pass().click()
        print('click')

    def input_username(self, username):
        self.get_username().send_keys(username)
        print('input username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input username')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('click')

    # ending
    def authorization(self):
        self.get_current_url()
        self.click_profile_button()
        self.click_enter_with_pass()
        self.input_username('glagol.job@mail.ru')
        self.input_password('Testuser123')
        self.click_enter_button()
        self.assert_word(self.get_main_word(), 'Популярные товары')

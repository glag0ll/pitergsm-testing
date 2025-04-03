from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from selenium.webdriver.common.action_chains import ActionChains


class Laptops_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    menu = "//a[contains(@class, 'hcat__link') and contains(@href, '/catalog/tablets-and-laptops') and normalize-space(text())='Планшеты и ноутбуки']"
    all_laptops_button = "//a[contains(@class, 'hcatsublist__link') and @href='/catalog/tablets-and-laptops/laptops/']//span[contains(@class, 'hcatsublist__text') and normalize-space()='Все ноутбуки']"


    #getters
    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.menu)))

    def get_all_laptops_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_laptops_button)))

    def point_menu(self):
        self.action.move_to_element(self.get_menu()).perform()
        print('наводимся на меню')

    def click_all_laptops(self):
        self.get_all_laptops_button().click()
        print("кнопка на категорию всех ноутбуков нажата")

    def open_laptops_category(self):
        self.get_current_url()
        self.point_menu()
        self.click_all_laptops()


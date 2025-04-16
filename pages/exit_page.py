from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

class Exit_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    place_order = "//a[contains(@class, 'cartplate__btn') and @href='/personal/cart/' and normalize-space()='Оформить']"
    delete = '//*[@id="basket_container"]/div[2]/div[1]/div[1]/div[4]/a'
    exit = "//a[@href='/personal/profile/?logout=yes' and normalize-space()='Выйти']"

    # getters
    def get_place_order(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.place_order))
        )

    def get_delete_buttons(self):
        try:
            return WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, self.delete)))
        except TimeoutException:
            return []

    def get_exit(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.exit))
        )

    # actions
    def click_place_order(self):
        self.get_place_order().click()
        print("переход к оформлению заказа")

    def click_delete(self):
        while True:
            delete_buttons = self.get_delete_buttons()
            if not delete_buttons:
                break
            button = delete_buttons[-1]
            try:
                button.click()
                WebDriverWait(self.driver, 10).until(EC.staleness_of(button))
                print("товар удален")
            except Exception as e:
                raise Exception(f"ошибка удаления: {str(e)}")

    def click_exit(self):
        self.get_exit().click()
        print("выход из аккаунта")

    def full_exit(self):
        self.get_current_url()
        self.click_place_order()
        self.click_delete()
        self.click_exit()
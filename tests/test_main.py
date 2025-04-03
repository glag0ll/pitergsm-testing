from pages.add_laptop_page import Add_laptop
from pages.add_smartphone import Add_smartphone
from pages.cart_page import Cart_page
from pages.laptops_page import Laptops_page
from pages.login_page import Login_page


def test_1(set_up):

    driver = set_up
    print('start test_1')

    login = Login_page(driver)
    login.authorization()

    all_laptops = Laptops_page(driver)
    all_laptops.open_laptops_category()

    buy_laptop = Add_laptop(driver)
    buy_laptop.add_laptop()

    buy_smartphone = Add_smartphone(driver)
    buy_smartphone.add_smartphone()

    cart = Cart_page(driver)
    cart.cart_checkout()
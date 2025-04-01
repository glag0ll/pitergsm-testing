from pages.login_page import Login_page


def test_1(set_up):

    driver = set_up
    print('start test_1')

    login = Login_page(driver)
    login.authorization()


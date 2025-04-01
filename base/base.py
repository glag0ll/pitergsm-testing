import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('good value')

    def get_screen(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = now_date + '.png'
        self.driver.save_screenshot('/home/glagol/AquaProjects/project2/screenshots/' + name_screen)

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('get value url')
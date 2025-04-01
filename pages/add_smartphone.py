from base.base import Base


class Add_smartphone(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    smartphones_page = "//a[contains(@class, 'hcat__link') and contains(@class, 'js_hcat-sub-trigger') and @href='/catalog/phones/' and normalize-space(text())='Смартфоны']"
    first_price = "//input[contains(@class, 'js_range_from') and contains(@class, 'filter-input__field--from') and @name='arrFilter_P1_MIN']"
    second_price = "//input[contains(@class, 'js_range_to') and contains(@class, 'filter-input__field--to') and @name='arrFilter_P1_MAX']"

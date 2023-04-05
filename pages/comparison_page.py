from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ComparisonPage(BasePage):
    # чисто сторінка порівняння
    # кількість товарів в порівнянні
    selected_goods_comparison = (By.XPATH, "//div[@class='product__heading']")



    def __init__(self, driver):
        super().__init__(driver)

    def search(self, keyword):
        search_input = self.get_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(keyword)
        # search_input.submit()

    # def click(self, element):
    #     search_input = self.get_element(element)
    #     search_input.click()

    def get_results(self):
        return self.get_elements(*self.RESULTS)
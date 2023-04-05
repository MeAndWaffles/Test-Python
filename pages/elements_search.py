from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ElementsSearch(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[contains(@name,'search')]")
    RESULTS = (By.XPATH, "//h1[contains(@class,'catalog-heading ng-star-inserted')][contains(.,'Nokia')]")

    def is_title_matches(self):
        return "ROZETKA™" in self.driver.title

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, keyword):
        search_input = self.get_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(keyword)
        # search_input.submit()

    def get_results(self):
        return self.get_elements(*self.RESULTS)

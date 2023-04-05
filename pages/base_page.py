from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://rozetka.com.ua/"

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_presence_of_element_located(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_for_visibility_of_element_located(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def open(self):
        self.driver.get(self.base_url)

    # def is_title_matches(self):
    #     return "Google" in self.driver.title

    def get_elements_text(self, *locator):
        elements = self.wait_for_visibility_of_element_located(locator)
        return [element.text for element in elements]

    def get_elements(self, *locator):
        return self.wait_for_visibility_of_element_located(locator)

    def get_elements2(self, *locator):
        return self.wait_for_visibility_of_element_located(locator)

    def get_element(self, locator):
        return self.wait_for_visibility_of_element_located(locator)

    def get_title(self):
        return self.driver.title

    def click(self, element):
        search_input = self.get_element(element)
        search_input.click()
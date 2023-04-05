from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.mylist import MyList
import time
import re

class Helper(BasePage):
    # хелпер з методами


    def click(self, element):
        search_input = self.get_element(element)
        search_input.click()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def create_new_list(self):
        return Helper()

    def is_title_matches(self, text):
        return text in self.driver.title

    def assert_num_elements(driver, locator, expected_num):
        """
        Asserts that the number of elements found by the given locator is equal to the expected number.
        Raises AssertionError if the number of elements is not equal to the expected number.
        """
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))
        actual_num = len(elements)
        assert actual_num == expected_num, f"Expected {expected_num} elements, but found {actual_num}"


    def enter_text(self, locator, text):
        """
        Enters the given text into the given element and waits for the element to be visible.
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """
        Waits for the element to be visible and returns its text
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def assert_text(self, actual_text, expected_text):
        assert actual_text == expected_text, f"Actual text: {actual_text}, but expected: {expected_text}"

    def assert_product_count(self, product_count: int, *locator, timeout=10):
        """
        Asserts that the number of products displayed for the given locator is equal to the given count.
        """
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        filtered_text = [re.sub("[^0-9]", "", element.text) for element in elements]
        count = sum([int(text) for text in filtered_text])
        assert count == product_count, f"Expected {product_count} products, but got {count}"

    def is_element_not_present(driver, locator, timeout=3):
        """
        Перевіряє чи відсутній елемент на сторінці

        :param driver: екземпляр WebDriver
        :param by: метод пошуку елемента (наприклад, By.XPATH, By.ID і т.д.)
        :param locator: локатор елемента
        :param timeout: час очікування, за замовчуванням 10 секунд
        :return: повертає True, якщо елемент відсутній, інакше повертає False
        """

        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator)))
            return False
        except:
            return True

    # def assert_list_items(driver, locator, expected_items):
    #     my_list = MyList()
    #     my_list_items = my_list.get_list_items()
    #     actual_items = [item.text for item in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator))]
    #     assert actual_items == expected_items, f"Expected {expected_items}, but found {actual_items}"
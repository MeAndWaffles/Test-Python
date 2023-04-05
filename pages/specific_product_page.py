from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SpecificProductPage(BasePage):
    # ще не знаю
    # вибір телефона конкретно
    filter_Rozetka = (By.XPATH, "//a[contains(@title,'(SM-M336BZBGSEK)')]/span[@class='goods-tile__title']")
    # з права кнопка фільтрувати по продавцу ASUS
    filter_ASUS = (By.XPATH, "//a[@data-id='ASUS']")
    # фільтери які появляються коли увімкнені
    list_filters_on = (By.XPATH, "//a[@class='catalog-selection__link']")
    # фільтери очистити все
    list_filters_ofAll = (By.XPATH, "//button[@class='catalog-selection__link catalog-selection__link_type_reset']")
    # "веси" порівняння товарів, перший товар приставка
    goods_console_one = (By.XPATH, "//div[@data-goods-id='359177217']//button[@class='compare-button ng-star-inserted']")
    # "веси" порівняння товарів, другий товар приставка
    goods_console_two = (By.XPATH, "//div[@data-goods-id='368982156']//button[@class='compare-button ng-star-inserted']")
    # "веси" перейти до порівнювання
    open_window_comparison = (By.XPATH, "//li[contains(@class,'comparison')]//button[contains(@class,'header__button ng-star-inserted')]")
    # "веси" у вікні перейти на нову сторінку
    Go_comparison = (By.XPATH, "//a[@class='comparison-modal__link']")
    # "бажане" добавити до бажаних
    to_favorite = (By.XPATH, "//div[@data-goods-id='333254422']//button[contains(@class,'wish-button')]")
    # "бажане" відображається вікно входа коли добавляєш до бажаного, елемент назви входа
    entry_login_window = (By.XPATH, "//h3[@class='modal__heading']")



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
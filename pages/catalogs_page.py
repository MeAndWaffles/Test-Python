from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    # це де смартфони, телефони, електроніка / думаю зробити один файл для всіх каталогів!!
    # перейти чисто до телофонів
    Go_Page_phones = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'mobile-phones/c80003/')][contains(@class,'heading')]")
    # перейти чисто game consoles
    Go_game_consoles = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'/consoles/c80020/')][contains(@class,'heading')]")
    # перейти велика побутова техніка
    Go_large_appliances = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'/bigbt/c80080/')][contains(@class,'heading')]")
    # перейти до холодильників
    Go_fridge = (By.XPATH, "//a[contains(@href,'/refrigerators/c80125/')]//span[@class='portal-navigation__link-text']/parent::*")
    # перейти чисто до ноутов
    Go_Page_laptops = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'notebooks/c80004/')][contains(@class,'heading')]")
    # перейти меблів
    Go_furniture = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'/mebel/c152458/')][contains(@class,'heading')]")
    # перейти крісла
    Go_chairs = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'/c4657815/')][contains(@class,'heading')]")
    # перейти крісла геймерські
    Go_gaming_chairs = (By.XPATH, "//a[contains(@href,'kresla/c4657827/')]//span[@class='portal-navigation__link-text']/parent::*")
    # перейти автоелектроніка
    Go_car_electronics = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'/c280596/')][contains(@class,'heading')]")
    # перейти автомобільні монітори
    Go_car_monitors = (By.XPATH, "//a[contains(@href,'avtomonitory/c280598/')]//span[@class='portal-navigation__link-text']/parent::*")
    # перейти до ванн
    Go_bathroom_plumbing = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'bathroom/c80106/')][contains(@class,'heading')]")
    # перейти до душових
    Go_shower_set = (By.XPATH, "//a[contains(@href,'/c116943/')]//span[@class='portal-navigation__link-text']/parent::*")
    # перейти до садових
    Go_garden = (By.XPATH, "//div[contains(@class,'tile-cats')]/a[contains(@href,'tech/c152459/')][contains(@class,'heading')]")
    # перейти до ланцюгові пили
    Go_chain_saws = (By.XPATH, "//a[contains(@href,'c155515/')]//span[@class='portal-navigation__link-text']/parent::*")
    # перейти до електропили
    Go_electric_saws = (By.XPATH, "//a[contains(@href,'c4674576/')]//span[@class='portal-navigation__link-text']/parent::*")


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
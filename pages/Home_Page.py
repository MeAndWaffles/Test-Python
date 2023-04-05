from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # перейти до компи та ноути
    Go_Computers_laptops = (By.XPATH, "//li[contains(@class,'menu-categories__item n')]/a[contains(@href,'c80253/')]")
    # перейти до смартфони, телефони, електроніка
    Go_smartphones_phones_electronics = (By.XPATH, "//li[contains(@class,'menu-categories__item n')]/a[contains(@href,'c4627949/')][@class='menu-categories__link']")
    # перейти до товари для геймерів
    Go_goods_for_gamers = (By.XPATH, "//li[contains(@class,'menu-categories__item n')]/a[contains(@href,'c80261/')][@class='menu-categories__link']")
    # перейти до побутова техніка
    Go_household_appliances = (By.XPATH, "//a[@class='menu-categories__link'][contains(@href,'bt')]")
    # перейти до логіна
    Go_login = (By.XPATH, "//li[contains(@class,'item--user')]//button[@class='header__button ng-star-inserted']")
    # строка пошти
    mail_login = (By.XPATH, "//input[@formcontrolname='login']")
    # строка пароля
    password_login = (By.XPATH, "//input[@formcontrolname='password']")
    # строка помилкі коли не правильний емайл, телефон
    error_login = (By.XPATH, "//p[@class='error-message ng-star-inserted']")
    # перейти до товарів для дому
    Go_household_goods = (By.XPATH, "//a[@class='menu-categories__link'][contains(@href,'/c2394287/')]")
    # перейти до інструменти та автотовари
    Go_tools_and_auto_goods = (By.XPATH, "//a[@class='menu-categories__link'][contains(@href,'/c4627858/')]")
    # перейти до сантехніка та ремонти
    Go_plumbing_and_repairs = (By.XPATH, "//a[@class='menu-categories__link'][contains(@href,'/c4628418/')]")
    # перейти до дача сад город
    Go_dacha_garden_garden = (By.XPATH, "//a[@class='menu-categories__link'][contains(@href,'/c2394297/')]")



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
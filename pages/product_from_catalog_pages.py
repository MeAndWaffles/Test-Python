from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductFromCatalogPages(BasePage):
    # тут коли переходим на більш конкретний товар
    # з права кнопка фільтрувати по продавцу розетка
    filter_Rozetka = (By.XPATH, "//a[@data-id='Rozetka']")
    # з права кнопка фільтрувати по продавцу ASUS
    filter_ASUS = (By.XPATH, "//a[@data-id='ASUS']")
    # фільтери які появляються коли увімкнені
    list_filters_on = (By.XPATH, "//a[@class='catalog-selection__link']")
    # фільтери очистити все
    list_filters_ofAll = (By.XPATH, "//button[@class='catalog-selection__link catalog-selection__link_type_reset']")
    # вибір телефона конкретно
    specific_Phone = (By.XPATH, "//a[contains(@title,'(SM-M336BZBGSEK)')]/span[@class='goods-tile__title']")
    # вибір стільця і добавлення в корзину перший
    add_chair_in_shopping_cart_one = (By.XPATH, "//div[@data-goods-id='329710705']//button[contains(@class,'buy-button')]")
    # вибір стільця і добавлення в корзину перший
    add_chair_in_shopping_cart_two = (By.XPATH, "//div[@data-goods-id='167365311']//button[contains(@class,'buy-button')]")
    # перейти до корзини активної
    Go_shopping_cart = (By.XPATH, "//button[contains(@class,'button--active')]")
    # елемент що бере всі товари в корзині
    all_in_goods_shopping_cart = (By.XPATH, "//a[@class='cart-product__title']")
    # вибір монітора для автомобіля
    add_car_monitors_in_shopping_cart = (By.XPATH, "//div[@data-goods-id='110475640']//button[contains(@class,'buy-button')]")
    # в корзині три крапкі
    three_dots_in_shopping_cart = (By.XPATH, "//button[contains(@class,'toggle--context')]")
    # вікно після нажаття трьох крапок до товара в корзині, щоб удалити кнопка
    product_removal_shopping_cart = (By.XPATH, "//button[contains(@class,'button--link')]")
    # картинка у вікні товарів, коли товарів немає
    window_picture_shopping_cart = (By.XPATH, "//img[@class='cart-dummy__illustration']")
    # вибір душевої та добавлення в корзину
    add_shower_set_in_shopping_cart = (By.XPATH, "//div[@data-goods-id='57759933']//button[contains(@class,'buy-button')]")
    # елемент титульної в середині, а точніше його назва на сторінці конкретного товару
    product_name_on_its_page = (By.XPATH, "//h1[@class='product__title']")
    # елемент в фільтрі для максимальної ціни
    filter_maximum_price = (By.XPATH, "//input[contains(@class,'ng-valid')][@formcontrolname='max']")
    # елемент в фільтрі для мінімальної ціни
    filter_minimum_price = (By.XPATH, "//input[contains(@class,'ng-valid')][@formcontrolname='min']")
    # елемент цін товарів загальний
    get_price = (By.XPATH, "//span[@class='goods-tile__price-value']")
    # фільтр є в наявності
    is_available = (By.XPATH, "//a[@data-id='Є в наявності']")
    # елемент ціни товара
    get_price_one = (By.XPATH, "/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[2]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span/text()")
    # елемент ціни товара
    get_price_two = (By.XPATH, "//A[@title='Пила ланцюгова GOOD LUCK SUPER 2000-405 (111676)']/span")

    # &&&&&??????
    # з права кнопка фільтрувати по продавцу ASUS
    # filter_ASUS = (By.XPATH, "//a[@data-id='ASUS']")
    # # фільтери які появляються коли увімкнені
    # list_filters_on = (By.XPATH, "//a[@class='catalog-selection__link']")
    # # фільтери очистити все
    # list_filters_ofAll = (By.XPATH, "//button[@class='catalog-selection__link catalog-selection__link_type_reset']")
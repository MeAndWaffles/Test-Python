from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.product_from_catalog_pages import ProductFromCatalogPages
from utils.helpers import Helper


def test_ShoppingCartRemove(browser):
    action = Helper(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productPage = ProductFromCatalogPages(browser)

    homePage.open()

    action.click(homePage.Go_tools_and_auto_goods)

    action.click(catalogPage.Go_car_electronics)

    action.click(catalogPage.Go_car_monitors)

    action.click(productPage.add_car_monitors_in_shopping_cart)

    action.click(productPage.Go_shopping_cart)

    action.click(productPage.three_dots_in_shopping_cart)

    action.click(productPage.product_removal_shopping_cart)

    action.assert_num_elements(productPage.window_picture_shopping_cart, 1)

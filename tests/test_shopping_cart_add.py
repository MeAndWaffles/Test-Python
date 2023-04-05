from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.product_from_catalog_pages import ProductFromCatalogPages
from utils.helpers import Helper


def test_ShoppingCartAdd(browser):
    action = Helper(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productPage = ProductFromCatalogPages(browser)

    homePage.open()

    action.click(homePage.Go_household_goods)
    action.click(catalogPage.Go_furniture)
    action.click(catalogPage.Go_chairs)
    action.click(catalogPage.Go_gaming_chairs)
    action.click(productPage.add_chair_in_shopping_cart_one)
    action.click(productPage.add_chair_in_shopping_cart_two)
    action.click(productPage.Go_shopping_cart)
    action.assert_num_elements(productPage.all_in_goods_shopping_cart, 2)

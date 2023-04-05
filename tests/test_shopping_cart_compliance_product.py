from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.product_from_catalog_pages import ProductFromCatalogPages
from utils.helpers import Helper


def test_ShoppingCartConformityProduct(browser):
    action = Helper(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productPage = ProductFromCatalogPages(browser)

    homePage.open()

    action.click(homePage.Go_plumbing_and_repairs)

    action.click(catalogPage.Go_bathroom_plumbing)

    action.click(catalogPage.Go_shower_set)

    action.click(productPage.add_shower_set_in_shopping_cart)

    action.click(productPage.Go_shopping_cart)

    productName = action.get_text(productPage.all_in_goods_shopping_cart)

    action.click(productPage.all_in_goods_shopping_cart)

    action.assert_text(productPage.get_element(productPage.product_name_on_its_page).text, productName)

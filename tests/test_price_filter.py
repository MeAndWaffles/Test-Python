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


    action.click(homePage.Go_dacha_garden_garden)

    action.click(catalogPage.Go_garden)

    action.click(catalogPage.Go_chain_saws)

    action.click(catalogPage.Go_electric_saws)

    action.click(productPage.is_available)

    action.enter_text(productPage.filter_minimum_price, "1700")
    action.enter_text(productPage.filter_maximum_price, "1800\n")

    action.click(productPage.list_filters_ofAll)
    action.is_element_not_present(productPage.list_filters_on)
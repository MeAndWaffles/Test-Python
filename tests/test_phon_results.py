from pages.base_page import BasePage
from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.product_from_catalog_pages import ProductFromCatalogPages
from utils.helpers import Helper

def test_PhonResults(browser):
    action = Helper(browser)
    basePage = BasePage(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productPage = ProductFromCatalogPages(browser)

    basePage.open()

    action.click(homePage.Go_smartphones_phones_electronics)

    action.click(catalogPage.Go_Page_phones)

    action.click(productPage.specific_Phone)

    action.is_title_matches("(SM-M336BZBGSEK)")
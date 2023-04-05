from pages.base_page import BasePage
from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.product_from_catalog_pages import ProductFromCatalogPages
from utils.helpers import Helper


def test_FilterDisplay(browser):
    action = Helper(browser)
    basePage = BasePage(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productpPage = ProductFromCatalogPages(browser)

    basePage.open()
    action.click(homePage.Go_Computers_laptops)

    action.click(catalogPage.Go_Page_laptops)

    action.click(productpPage.filter_Rozetka)
    action.assert_num_elements(productpPage.list_filters_on, 1)

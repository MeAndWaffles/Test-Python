from pages.base_page import BasePage
from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.specific_product_page import SpecificProductPage
from utils.helpers import Helper


def test_Favorite(browser):
    action = Helper(browser)
    basePage = BasePage(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    productPage = SpecificProductPage(browser)

    basePage.open()

    action.click(homePage.Go_household_appliances)

    action.click(catalogPage.Go_large_appliances)

    action.click(catalogPage.Go_fridge)

    action.click(productPage.to_favorite)

    action.assert_num_elements(productPage.entry_login_window, 1)

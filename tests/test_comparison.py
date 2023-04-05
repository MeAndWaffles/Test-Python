from pages.base_page import BasePage
from pages.catalogs_page import CatalogPage
from pages.Home_Page import HomePage
from pages.comparison_page import ComparisonPage
from pages.specific_product_page import SpecificProductPage
from utils.helpers import Helper


# from pages import catalog_computers_laptops, elements_search, Home_Page, laptops_page

def test_Comparison(browser):
    action = Helper(browser)
    basePage = BasePage(browser)
    catalogPage = CatalogPage(browser)
    homePage = HomePage(browser)
    comparisonPage = ComparisonPage(browser)
    productPage = SpecificProductPage(browser)

    basePage.open()

    action.click(homePage.Go_goods_for_gamers)

    action.click(catalogPage.Go_game_consoles)

    action.click(productPage.goods_console_one)

    action.click(productPage.goods_console_two)

    action.click(productPage.open_window_comparison)

    action.click(productPage.Go_comparison)

    action.assert_num_elements(comparisonPage.selected_goods_comparison, 2)

from pages.Home_Page import HomePage
from utils.helpers import Helper


def test_Login(browser):
    action = Helper(browser)
    homePage = HomePage(browser)

    homePage.open()

    action.click(homePage.Go_login)

    action.enter_text(homePage.mail_login, "12345\n")
    action.enter_text(homePage.password_login, "54321\n")
    action.assert_num_elements(homePage.error_login, 1)
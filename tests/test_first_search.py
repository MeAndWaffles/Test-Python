from pages.elements_search import ElementsSearch


def test_RozetkaSearchResults(browser):
    search_page = ElementsSearch(browser)
    search_page.open()
    print(search_page.get_title())
    assert search_page.is_title_matches()
    search_page.search('Nokia\n')
    print(search_page.get_title())
    assert search_page.get_results()

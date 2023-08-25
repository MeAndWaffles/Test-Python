from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()
    # input("Press any key to exit...")

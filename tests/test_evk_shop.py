import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.item_page import ItemPage
from pages.main_page import MainPage

def test_client_path(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    mp = MainPage(driver)
    mp.start()

    cp = CatalogPage(driver)
    cp.select_filter_options()

    ip = ItemPage(driver)
    ip.select_product()

    ch_p = CheckoutPage(driver)
    ch_p.confirm_purchase()
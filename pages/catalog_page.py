from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class CatalogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Locators
    parent_women_category = "//a[@class='js-nav-collapse']"
    women_shirts = "//a[@href='https://evkaliptica.com/shop/women/shirts']"
    filter_button = "//button[@class='filter__button']"
    size_checkbox = "//input[@value='9']"
    height_checkbox = "//input[@value='38']"
    color_checkbox = "//input[@value='10']"
    search_button = "//button[contains(text(), 'Искать')]"


    # Getters
    def get_parent_women_category(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.parent_women_category)))

    def get_women_shirts(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.women_shirts)))

    def get_filter_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_size_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.size_checkbox)))

    def get_height_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.height_checkbox)))

    def get_color_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.color_checkbox)))

    def get_search_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    # Actions
    def click_parent_women_category(self):
        self.get_parent_women_category().click()
        print("Click Parent Women Category")

    def click_women_shirts(self):
        self.get_women_shirts().click()
        print("Click Women Shirts")

    def click_filter_button(self):
        self.get_filter_button().click()
        print("Click Filter Button")

    def click_size_checkbox(self):
        self.get_size_checkbox().click()
        print("Click Size Checkbox")

    def click_height_checkbox(self):
        self.get_height_checkbox().click()
        print("Click Height Checkbox")

    def click_color_checkbox(self):
        self.get_color_checkbox().click()
        print("Click Color Checkbox")

    def click_search_button(self):
        self.get_search_button().click()
        print("Click Search Button")


    #Methods
    def get_filter_url(self):
        #Строим URL после применения фильтра
        base_url = "https://evkaliptica.com/shop/women/shirts"
        params = {
        "attributes":[9,38],
        "colors": [10],
        "prices[min]": 6480,
        "prices[max]": 8980
    }
        return self.build_url_with_params(base_url, params)


    def select_filter_options(self):
        # Предварительная проверка URL
        expected_url = self.get_filter_url()
        print(f"Expected URL: {expected_url}")

        self.get_current_url()
        self.click_parent_women_category()
        self.click_women_shirts()
        self.click_filter_button()
        self.click_size_checkbox()
        self.click_height_checkbox()
        self.click_color_checkbox()
        self.click_search_button()
        self.wait.until(EC.url_contains("attributes")) # Ждем применения фильтров
        self.assert_url(expected_url)


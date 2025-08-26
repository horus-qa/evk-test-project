from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base
from utils.logger import Logger


class MainPage(Base):

    url = 'https://evkaliptica.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    #Locators
    subscribe_window = "//div[@class='subscribe__content--close']"
    jivo_chat = "//jdiv[@id='jivo_close_button']"
    catalog_button = "//a[@href='https://evkaliptica.com/shop']"
    main_word = "//span[@itemprop='itemListElement']"

    #Getters
    def get_subscribe_window(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.subscribe_window)))

    def get_jivo_chat(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.jivo_chat)))

    def get_catalog_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_main_word(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.main_word)))


    #Actions
    def click_subscribe_window(self):
        self.get_subscribe_window().click()
        print("Close Subscribe Window")

    def click_jivo_chat(self):
        self.get_jivo_chat().click()
        print("Close Jivo Chat")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")


    #Methods
    def start(self):
        with allure.step("Start"):
            Logger.add_start_step(method='start')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_subscribe_window()
            self.click_jivo_chat()
            self.click_catalog_button()
            self.assert_word(self.get_main_word(), "КАТАЛОГ")
            Logger.add_end_step(url=self.driver.current_url,method='start')

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class ItemPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    #Locators
    product_1 = "//a[@data-product-id='294']"
    product_filter_height = "//label[contains(., '170')]"
    product_filter_size = "//label[contains(., '44-46')]"
    cart_button = "//button[@class='btn btn--green btn--full js-add-to-cart btn--sticky']"
    checkout_button = "//a[@id='js-cart-checkout']"
    page_name = "//h1[contains(text(),'Оформление заказа')]"

    #Характеристики товара
    item_name = "//a[@class='preview_item__name']"
    item_size = "//div[@class='preview_item__text']//div[b[contains(text(), 'Размер')]]"
    item_height = "//div[@class='preview_item__text']//div[b[contains(text(), 'Рост')]]"
    item_price = "(//div[@class='preview_item__price'])[1]"

    # Getters
    def get_product_1(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_filter_height(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_filter_height)))

    def get_product_filter_size(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_filter_size)))

    def get_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_checkout_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_page_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.page_name)))

    def get_item_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.item_name)))

    def get_item_size(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.item_size)))

    def get_item_height(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.item_height)))

    def get_item_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.item_price)))



    # Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("Click Product 1")

    def click_product_filter_height(self):
        self.get_product_filter_height().click()
        print("Click Product Filter Height")

    def click_product_filter_size(self):
        self.get_product_filter_size().click()
        print("Click Product Filter Size")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout Button")


    #Methods
    def select_product(self):

        self.get_current_url()
        self.click_product_1()
        self.click_product_filter_height()
        self.click_product_filter_size()
        self.click_cart_button()
        self.click_checkout_button()
        self.assert_word(self.get_page_name(), "ОФОРМЛЕНИЕ ЗАКАЗА")
        name = self.get_item_name().text.strip()
        size = self.get_item_size().text.split(":")[1].strip()
        height = self.get_item_height().text.split(":")[1].strip()
        price = self.get_item_price().text.strip().replace("\n", "").replace(" ", " ").replace("руб.", "руб.").strip()

        self.assert_item(name=name, size=size, height=height, price=price)

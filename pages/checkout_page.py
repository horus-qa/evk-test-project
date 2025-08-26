import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from faker import Faker

from base.base_class import Base
from utils.logger import Logger


class CheckoutPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.fake: Faker = Faker('ru_RU')

        self.input_address = "г Москва, ул Реутовская, д 3" #Шаблонный адрес


    #Locators
    address_field = "//input[@name='address']"
    first_name_field = "//input[@name='name']"
    last_name_field = "//input[@name='surname']"
    phone_field = "//input[@name='phone']"
    email_field = "//input[@name='email']"
    comment_field = "//textarea[@name='comment']"
    package_checkbox = "//input[@name='has_packages']"
    confirm_button = "//button[@class='btn btn--green']"

    #Цены для проверки
    product_price_value = "//span[@id='js-cart-products-price']"
    delivery_price_value = "//span[@id='js-cart-delivery-price']"
    discount_price_value = "//span[@id='js-cart-discount-price']"
    total_price_value = "//span[@id='js-cart-total-price']"


    #Getters
    def get_address_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_address_suggestion(self):
        path = f"//ul[@id='autoComplete_list_1']/li[normalize-space()='{self.input_address}']"
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, path)))

    def get_first_name_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_phone_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_email_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_comment_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_package_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.package_checkbox)))

    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    # Getters для цен
    def get_product_price_element(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.product_price_value)))

    def get_delivery_price_element(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.delivery_price_value)))

    def get_discount_price_element(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.discount_price_value)))

    def get_total_price_element(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.total_price_value)))

    #Actions
    def click_address_field(self):
        self.get_address_field().click()
        print("Click Address Field")

    def clear_address_field(self):
        address = self.get_address_field()
        address.send_keys(Keys.CONTROL + "a")
        address.send_keys(Keys.DELETE)
        print("Clear Address Field")

    def input_address_value(self):
        self.get_address_field().send_keys(self.input_address)
        print(f"Input Address: {self.input_address}")

    def click_address_confirm(self):
        self.get_address_suggestion().click()
        print("Click Address Suggestion")

    def input_first_name(self, value):
        self.get_first_name_field().send_keys(value)
        print(f"Input First Name: {value}")

    def input_last_name(self, value):
        self.get_last_name_field().send_keys(value)
        print(f"Input Last Name: {value}")

    def input_phone(self, value):
        field = self.get_phone_field()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        for char in value:
            field.send_keys(char)
        print(f"Input Phone: {value}")

    def input_email(self, value):
        self.get_email_field().send_keys(value)
        print(f"Input Email: {value}")

    def input_comment(self, value):
        self.get_comment_field().send_keys(value)
        print(f"Input Comment: {value}")

    def click_package_checkbox(self):
        self.get_package_checkbox().click()
        print("Click Package Checkbox")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click Confirm Button")

    #Method
    def confirm_purchase(self):
        with allure.step("Confirm Purchase"):
            Logger.add_start_step(method='confirm_purchase')
            self.get_current_url()

            # Сгенерировать фейковые данные
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            phone = self.fake.numerify('9#########')
            email = self.fake.email()
            comment = "Тестовый заказ"

            print(f"[Test Data] {first_name} {last_name}, {phone}, {email}")

            # Заполнение формы
            self.click_address_field()
            self.clear_address_field()
            self.input_address_value()
            self.click_address_confirm()

            self.input_first_name(first_name)
            self.input_last_name(last_name)
            self.input_phone(phone)
            self.input_email(email)
            self.input_comment(comment)

            self.click_package_checkbox()
            self.check_total_price_by_elements(
                product_element=self.get_product_price_element(),
                delivery_element=self.get_delivery_price_element(),
                discount_element=self.get_discount_price_element(),
                total_element=self.get_total_price_element()
            )
            # self.click_confirm_button()
            Logger.add_end_step(url=self.driver.current_url, method='confirm_purchase')


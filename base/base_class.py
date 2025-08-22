from urllib.parse import urlencode

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверяемое слово совпадает")

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Проверяемый URL совпадает")

    def build_url_with_params(self, base_url: str, params: dict) -> str:
        """
        Строим URL с параметрами из словаря
        base_url: базовый URL без параметров
        params: словарь с параметрами {имя: значение}
        """
        # Преобразуем параметры в формат для URL
        query_params = {}
        for key, value in params.items():
            if isinstance(value, list):
                # Для массивов используем ключи с []
                query_params[f"{key}[]"] = value
            else:
                query_params[key] = value

        # Создаем query string
        query_string = urlencode(query_params, doseq=True)
        return f"{base_url}?{query_string}"

    """Method assert item characteristics"""

    def assert_item(self, name=None, size=None, height=None, price=None):
        if name:
            assert name == "РУБАШКА WHITE STRIPE", f"Неверное наименование: {name}"
        if size:
            assert size == "44-46", f"Неверный размер: {size}"
        if height:
            assert height == "170", f"Неверный рост: {height}"
        if price:
            assert price == "6 480 руб.", f"Неверная цена: {price}"
        print("Проверка товара прошла успешно")


    """Method assert item price"""

    def get_price_int(self, element):
        """Преобразуем текст с рублями и пробелами в целое число"""
        text = element.text.strip()
        digits = ''.join(c for c in text if c.isdigit())
        return int(digits) if digits else 0

    def check_total_price_by_elements(self, product_element, delivery_element, discount_element, total_element):
        """Сравниваем итоговую сумму"""
        product_price = self.get_price_int(product_element)
        delivery_price = self.get_price_int(delivery_element)
        discount_price = self.get_price_int(discount_element)
        total_price = self.get_price_int(total_element)

        expected_total = product_price + delivery_price - discount_price

        print(
            f"Цена товара: {product_price} р., Доставка: {delivery_price} р., Скидка: {discount_price} р., Ожидаемая сумма: {expected_total}р., Фактическая сумма: {total_price} р.")

        assert total_price == expected_total, f"Итоговая сумма некорректна: ожидается {expected_total}, отображается {total_price}"
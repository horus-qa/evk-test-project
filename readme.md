# EVK Test Project

Автоматизированный UI-тест для интернет-магазина [evkaliptica.com](https://evkaliptica.com/) с использованием **Selenium**, **Pytest** и **Page Object Model**. 
Тест реализован на Python и предназначен для проверки крит.пути пользователя.

## 📁 Структура проекта

<pre> <code>
evk-test-project/ 
├── base/ # Базовые классы и логика 
├── pages/ # Page Object'ы 
├── tests/ # Тест-кейсы 
├── screenshots/ # Скриншоты 
├── requirements.txt # Зависимости 
└── README.md </code> </pre>


## 🚀 Как запустить

1. Клонировать репозиторий
````
git clone https://github.com/horus-qa/evk-test-project.git

cd evk-test-project
````
2. Создать и активировать виртуальное окружение
````
python -m venv venv
````
Для Windows:
````
venv\Scripts\activate
````

Для macOS/Linux:
````
source venv/bin/activate
````

3. Установить зависимости
````
pip install -r requirements.txt
````

4. Запустить тест
````
pytest tests/
````

## 📊 Скриншоты Allure
| Overview Dashboard       | Test Suite Structure     |
|:------------------------:|:------------------------:|
| <img src="Allure-Report.png" width="400"> | <img src="Allure-Report-08-26.png" width="400"> |

## 🧰 Используемые технологии

* Python
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Faker
* Dotenv (для хранения переменных окружения)
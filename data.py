from locators.base_page_locators import BasePageLocators

class TestData:

    names = ['Игорь', 'Игорян']
    surnames = ['Лысиков', 'Лысикян']
    adresses = ['Пушкина', 'Колотушкина']
    buttons = [BasePageLocators.order_button_upper_menu, BasePageLocators.order_button_page_down]

class Urls:
    expected_samokat_url = "https://qa-scooter.education-services.ru/"
    expected_dzen_url = "https://dzen.ru/"
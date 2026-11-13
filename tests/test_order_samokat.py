import allure
import pytest
import random as r
from pages.order_samokat_page import OrderSamokatPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators

@allure.title('Проверка оформления заказа')
@allure.description('На базовой странице ищем элемент заказа через параметизацию, вносим все необходимые наборы данных, оформляем заказ и проверяем ссылки в шапке страницы')
class TestOrderSamokat:
    names = ['Игорь', 'Игорян']
    surnames = ['Лысиков', 'Лысикян']
    adresses = ['Пушкина', 'Колотушкина']
    buttons = [BasePageLocators.order_button_upper_menu, BasePageLocators.order_button_page_down]
    
    @pytest.mark.parametrize('name,surname,adress,buttons', list(zip(names, surnames, adresses, buttons)))
    def test_order(self, driver, name, surname, adress, buttons):
        phone = str(r.randint(10000000000, 99999999999))
        page = OrderSamokatPage()
        page.click_order_button(driver, buttons)
        page.order_samokat(driver, name, surname, adress, phone)
        assert "Заказ оформлен" in driver.find_element(*OrderPageLocators.accept_message).text
        current_link = page.click_samokat_logo(driver)
        assert current_link == "https://qa-scooter.education-services.ru/"
        current_link = page.click_dzen(driver)
        assert current_link == "https://dzen.ru/"
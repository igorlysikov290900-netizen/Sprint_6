import pytest
import random as r
from pages.order_samokat_page import OrderSamokatPage
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestOrderSamokat:
    name_1 = 'Игорь'
    name_2 = 'Игорян'
    names = [name_1, name_2]
    surname_1 = 'Лысиков'
    surname_2 = 'Лысикян'
    surnames = [surname_1, surname_2]
    adress_1 = 'Пушкина'
    adress_2 = 'Колотушкина'
    adresses = [adress_1, adress_2]
    number_1 = str(r.randint(1000000000, 9999999999))
    number_2 = str(r.randint(1000000000, 9999999999))
    numbers = [number_1, number_2]
    
    @pytest.mark.parametrize('name,surname,adress,phone', [names, surnames, adresses, numbers])
    def test_order(self, name, surname, adress, phone):
        test_order_samokat = OrderSamokatPage
        test_order_samokat.order_samokat(name, surname, adress, phone)
        assert OrderPageLocators.accept_message == "Заказ оформлен"
        test_order_samokat.click_samokat_logo()
        assert current_link == "https://qa-scooter.education-services.ru/"
        test_order_samokat.click_samokat_logo()
        assert current_link == "https://dzen.ru/"
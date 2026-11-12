import pytest
import random as r
from pages.order_samokat_page import OrderSamokatPage
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestOrderSamokat:
    names = ['Игорь', 'Игорян']
    surnames = ['Лысиков', 'Лысикян']
    adresses = ['Пушкина', 'Колотушкина']
    
    @pytest.mark.parametrize('name,surname,adress', list(zip(names, surnames, adresses)))
    def test_order(self, driver, name, surname, adress):
        phone = str(r.randint(10000000000, 99999999999))
        page = OrderSamokatPage()
        page.click_order_button(driver)
        page.order_samokat(driver, name, surname, adress, phone)
        assert driver.find_element(*OrderPageLocators.accept_message).text == "Заказ оформлен"
        current_link = page.click_samokat_logo(driver)
        assert current_link == "https://qa-scooter.education-services.ru/"
        current_link = page.click_dzen(driver)
        assert current_link == "https://dzen.ru/"
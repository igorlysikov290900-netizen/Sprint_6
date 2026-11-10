import random as r
import pytest
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderSamokatPage:
    def __init__(self):
        self.name_1 = 'Игорь'
        self.name_2 = 'Игорян'
        self.surname_1 = 'Lysikov'
        self.surname_2 = 'Lysikyan'
        self.adress_1 = 'Пушкина'
        self.adress_2 = 'Колотушкина'
        self.number_1 = f"{r.randint(1000000000, 9999999999)}"
        self.number_2 = f"{r.randint(1000000000, 9999999999)}"
        self.order_btn = BasePageLocators.order_button_upper_menu
        self.name_field = OrderPageLocators.name_field
        self.surname_field = OrderPageLocators.surname_field
        self.adress_field = OrderPageLocators.adress
        self.metro_station_list = OrderPageLocators.metro_station
        self.metro_station = OrderPageLocators.metro_station
        self.phone_number_field = OrderPageLocators.phone_number
        

    def click_order_button(self, driver):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_btn))
        driver.find_element(*self.order_btn).click()

    def send_order_keys(self, driver):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_btn))
        driver.find_element(*self.order_btn).click()
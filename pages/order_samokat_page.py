import random as r
import pytest
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderSamokatPage:
    def __init__(self):
        self.order_btn = BasePageLocators.order_button_upper_menu
        self.name_field = OrderPageLocators.name_field
        self.surname_field = OrderPageLocators.surname_field
        self.adress_field = OrderPageLocators.adress
        self.metro_station_list = OrderPageLocators.metro_station
        self.metro_station = OrderPageLocators.metro_station
        self.phone_number_field = OrderPageLocators.phone_number
        self.next_button = OrderPageLocators.next_button
        self.date_field = OrderPageLocators.date_field
        self.date = OrderPageLocators.date
        self.rent_time = OrderPageLocators.rent_time
        self.rent_time_button = OrderPageLocators.rent_time_button
        self.collor = OrderPageLocators.collor
        self.order_button = OrderPageLocators.order_button
        self.accept_button = OrderPageLocators.accept_button
        self.accept_message = OrderPageLocators.accept_message
        self.status_button = OrderPageLocators.status_button
        self.samokat_button = BasePageLocators.samokat_logo
        self.dzen_button = BasePageLocators.dzen_button
        

    def click_order_button(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.order_btn))
        driver.find_element(*self.order_btn).click()

    def order_samokat(self, driver, name, surname, adress, phone):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.name_field))
        driver.find_element(*self.name_field).send_keys(name)
        driver.find_element(*self.surname_field).send_keys(surname)
        driver.find_element(*self.adress_field).send_keys(adress)
        driver.find_element(*self.metro_station_list).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.metro_station))
        driver.find_element(*self.metro_station).click()
        driver.find_element(*self.phone_number_field).send_keys(phone)
        driver.find_element(*self.next_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.date_field))
        driver.find_element(*self.date_field).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.date))
        driver.find_element(*self.date).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.rent_time))
        driver.find_element(*self.rent_time).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.rent_time_button))
        driver.find_element(*self.rent_time_button).click()
        driver.find_element(*self.collor).click()
        driver.find_element(*self.order_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.accept_button))
        driver.find_element(*self.accept_button).click()

    def click_samokat_logo(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.samokat_button))
        driver.find_element(*self.samokat_button).click()
        current_link = driver.current_url
        return current_link

    def click_dzen(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.dzen_button))
        driver.find_element(*self.dzen_button).click()
        current_link = driver.current_url
        return current_link

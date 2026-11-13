import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderSamokatPage(BasePage):
    def __init__(self):
        super().__init__()
        self.name_field = OrderPageLocators.name_field
        self.surname_field = OrderPageLocators.surname_field
        self.adress_field = OrderPageLocators.adress
        self.metro_station_list = OrderPageLocators.metro_station_list
        self.metro_option = OrderPageLocators.metro_option
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

    @allure.step('Оформляем заказ')
    def order_samokat(self, driver, name, surname, adress, phone):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.name_field))
        driver.find_element(*self.name_field).send_keys(name)
        driver.find_element(*self.surname_field).send_keys(surname)
        driver.find_element(*self.adress_field).send_keys(adress)
        driver.find_element(*self.metro_station_list).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.metro_option))
        driver.find_element(*self.metro_option).click()
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

    def click_status_button(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.status_button))
        driver.find_element(*self.status_button).click()

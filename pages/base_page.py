import pytest
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс страницы авторизации
class BasePage:

    def click_question_button(self, driver, question_button, question_text):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(question_text))
        element = driver.find_element(*question_button)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*question_button).click()
        self.text = driver.find_element(*question_text).text
        return self.text

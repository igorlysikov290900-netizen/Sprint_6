import pytest
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс страницы авторизации
class BasePage:

    def click_question_button(self, question_button, question_text):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question_button))
        self.driver.find_element(*question_button).click()
        self.text = self.driver.find_element(*question_text).text
        return self.text

class TestBasePage:
    @pytest.mark.parametrize('question_button,question_text', [BasePageLocators.buttons, BasePageLocators.text])
    def test_check_question_text(self, question_button, question_text):
        check_question_text = BasePage
        check_question_text.click_question_button(self, question_button, question_text)
        assert self.text == question_text
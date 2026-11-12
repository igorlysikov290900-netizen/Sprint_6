import pytest
from pages.base_page import BasePage
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestBasePage:
    @pytest.mark.parametrize('question_button,question_text', list(zip(BasePageLocators.buttons, BasePageLocators.text)))
    def test_check_question_text(self, driver, question_button, question_text):
        check_question_text = BasePage()
        text = check_question_text.click_question_button(driver, question_button, question_text)
        assert text == driver.find_element(*question_text).text
import pytest
from pages.base_page import BasePage
from selenium import webdriver
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestBasePage:
    @pytest.mark.parametrize('question_button,question_text', [BasePageLocators.buttons, BasePageLocators.text])
    def test_check_question_text(self, question_button, question_text):
        check_question_text = BasePage
        check_question_text.click_question_button(question_button, question_text)
        assert self.text == question_text
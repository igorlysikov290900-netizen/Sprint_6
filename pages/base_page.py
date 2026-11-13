import allure
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс страницы авторизации
class BasePage:
    def __init__(self):
        self.cookie_accept = BasePageLocators.cookie_accept
        self.samokat_button = BasePageLocators.samokat_logo
        self.dzen_button = BasePageLocators.dzen_button


    @allure.step('Нажимаем на кнопку вопоса и получаем текст ответа')
    def click_question_button(self, driver, question_button, question_text):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BasePageLocators.cookie_accept))
        driver.find_element(*BasePageLocators.cookie_accept).click()
        element = driver.find_element(*question_button)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element) 
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(question_text))
        self.text = driver.find_element(*question_text).text
        return self.text


    @allure.step('Килкаем на страницу заказа')
    def click_order_button(self, driver, button):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BasePageLocators.cookie_accept))
        driver.find_element(*self.cookie_accept).click()
        driver.find_element(*button).click()

    @allure.step('Кликаем на лого самоката')
    def click_samokat_logo(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.samokat_button))
        driver.find_element(*self.samokat_button).click()
        current_link = driver.current_url
        return current_link

    @allure.step('Кликаем на лого яндекса')
    def click_dzen(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(self.dzen_button))
        driver.find_element(*self.dzen_button).click()
        current_link = driver.current_url
        return current_link

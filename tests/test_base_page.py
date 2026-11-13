import allure
import pytest
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators

@allure.title('Проверка соответствия текста вопросов с ожиданием') # декораторы
@allure.description('На базовой странице ищем элемент вопроса и проверяем, что его текст == тексту из параметизации')
class TestBasePage:
    expected_text = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    @pytest.mark.parametrize('question_button,question_text,expected_text', list(zip(BasePageLocators.buttons, BasePageLocators.text, expected_text)))
    def test_check_question_text(self, driver, question_button, question_text, expected_text):
        page = BasePage()
        actual_text = page.click_question_button(driver, question_button, question_text)
        assert actual_text == expected_text
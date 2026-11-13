from selenium.webdriver.common.by import By

class BasePageLocators:
    order_button_upper_menu = (By.CLASS_NAME, 'Button_Button__ra12g')
    order_button_page_down = (By.XPATH, '//div[5]/button')
    how_much_it_cost_question = (By.ID, 'accordion__heading-0')
    how_much_it_cost_question_text = (By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')
    few_samokats_question = (By.ID, 'accordion__heading-1')
    few_samokats_question_text = (By.XPATH, '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]')
    rent_time_question = (By.ID, 'accordion__heading-2')
    rent_time_question_text = (By.XPATH, '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')
    samokat_rent_today_question = (By.ID, 'accordion__heading-3')
    samokat_rent_today_question_text = (By.XPATH, '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')
    rent_continue_question = (By.ID, 'accordion__heading-4')
    rent_continue_question_text = (By.XPATH, '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')
    samokat_charger_question = (By.ID, 'accordion__heading-5')
    samokat_charger_question_text = (By.XPATH, '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]')
    order_cancel_question = (By.ID, 'accordion__heading-6')
    order_cancel_question_text = (By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')
    dileviry_out_of_mkad_question = (By.ID, 'accordion__heading-7')
    dileviry_out_of_mkad_question_text = (By.XPATH, '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]')
    buttons = [how_much_it_cost_question, few_samokats_question, rent_time_question, samokat_rent_today_question, rent_continue_question, samokat_charger_question, order_cancel_question, dileviry_out_of_mkad_question]
    text = [how_much_it_cost_question_text, few_samokats_question_text, rent_time_question_text, samokat_rent_today_question_text, rent_continue_question_text, samokat_charger_question_text, order_cancel_question_text, dileviry_out_of_mkad_question_text]
    samokat_logo = (By.XPATH, '//a[2]/img')
    dzen_button = (By.XPATH, '//img')
    cookie_accept = (By.XPATH, '//button[text()="да все привыкли"]')
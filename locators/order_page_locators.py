from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = (By.XPATH, '//div[2]/div[1]/input')
    surname_field = (By.XPATH, '//div[2]/div[2]/input')
    adress = (By.XPATH, '//div[2]/div[3]/input')
    metro_station = (By.XPATH, '//div[4]/div/div/input')
    phone_number = (By.XPATH, '//div[5]/input')
    next_button = (By.XPATH, '//button[text()="Далее"]')
    date_field = (By.XPATH, '//div[1]/div/input')
    date = (By.XPATH, '//div[2]/div[4]')
    rent_time = (By.XPATH, '//div[text()="* Срок аренды"]')
    rent_time_button = (By.XPATH, '//div[text()="сутки"]')
    collor = (By.ID, 'black')
    accept_button = (By.XPATH, '//button[text()="Да"]')
    order_button = (By.XPATH, '//div[3]/button[2]')
    accept_message = (By.XPATH, '//div[text()="Заказ оформлен"]')
    status_button = (By.XPATH, '//button[text()="Посмотреть статус"]')
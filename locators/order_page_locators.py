from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = (By.XPATH, '//div[2]/div[1]/input')
    surname_field = (By.XPATH, '//div[2]/div[2]/input')
    adress = (By.XPATH, '//div[2]/div[3]/input')
    metro_station_list = (By.XPATH, '//div[4]/div/div/input')
    metro_station = (By.XPATH, '//button[text()="Черкизовская"]')
    phone_number = (By.XPATH, '//div[5]/input')
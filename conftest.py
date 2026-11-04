import pytest
from selenium import webdriver

url = 'https://qa-scooter.education-services.ru/'

@pytest.fixture
def driver():
    driver = webdriver.Firefox
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
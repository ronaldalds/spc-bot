from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable,
    alert_is_present,
)


class Mk:
    def __init__(self, operation: str, password: str, secret: str, url: str):
        self._operation: str = operation
        self._password: str = password
        self._secret: str = secret
        self._driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self._wdw = WebDriverWait(self._driver, 600)
        self._mouse = ActionChains(self._driver)
        self._driver.get(url)

    def click(self, xpath: str):
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).pause(5).click().pause(5).perform()

    def write(self, xpath: str, text: str):
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).pause(2).send_keys(text).pause(2).perform()

    def login(self):
        self._driver.find_element(
            By.XPATH, '//input[@placeholder="Nome do usuário"]').send_keys(self._username)
        self._driver.find_element(
            By.XPATH, '//input[@placeholder="Senha"]').send_keys(self._password)
        self._driver.find_element(By.XPATH, '//button[@name="user"]').click()

    def close(self):
        self._driver.close()

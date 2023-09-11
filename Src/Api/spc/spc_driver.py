import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import (
    alert_is_present,
)


class Spc:
    def __init__(self, operation: str, password: str, secret: str, url: str):
        self._operation: str = operation
        self._password: str = password
        self._secret: str = secret
        largura = 1280
        altura = 960
        options = webdriver.ChromeOptions()
        options.add_argument("--port=4444")
        options.add_argument('--no-sandbox')
        options.add_argument(f"--window-size={largura},{altura}")
        options.add_argument('--headless')
        self._driver = webdriver.Chrome(
            options=options
            )
        self._wdw = WebDriverWait(self._driver, 300)
        self._mouse = ActionChains(self._driver)
        self._driver.get(url)

    def click(self, xpath: str):
        time.sleep(5)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).click().perform()
        time.sleep(5)

    def dbclick(self, xpath: str):
        time.sleep(5)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).double_click().perform()
        time.sleep(5)

    def write(self, xpath: str, text: str):
        time.sleep(5)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).click().send_keys(text).perform()
        time.sleep(5)

    def text(self, xpath: str) -> str:
        value = self._driver.find_element(By.XPATH, xpath).get_attribute("value")
        return value

    def include(self):
        self._wdw.until(alert_is_present())
        self._driver.switch_to.alert.accept()
        time.sleep(5)

    def login(self):
        self.write('//*[@id="j_username"]', self._operation)
        self.write('//*[@id="j_password"]', self._password)
        self.click('//*[@id="submitButton"]')
        self.write('//*[@id="passphrase"]', self._secret)
        self.click('//*[@id="submitButton"]')

    def close(self):
        self._driver.quit()

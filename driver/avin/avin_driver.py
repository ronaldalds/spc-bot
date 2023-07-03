from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import (
    alert_is_present,
)


class Avin:
    def __init__(self, username: str, password: str, url: str, headless: bool = False):
        self._username: str = username
        self._password: str = password
        capabilities = DesiredCapabilities.CHROME.copy()
        largura = 1280
        altura = 960
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": os.path.join(os.getcwd(), 'process', 'downloads'),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        })
        options.add_argument(f"--window-size={largura},{altura}")
        options.headless = headless
        self._driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            desired_capabilities=capabilities,
            options=options
            )
        self._wdw = WebDriverWait(self._driver, 300)
        self._mouse = ActionChains(self._driver)
        self._driver.get(url)

    def click(self, xpath: str):
        time.sleep(2)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).click().perform()
        time.sleep(2)

    def dbclick(self, xpath: str):
        time.sleep(2)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).double_click().perform()
        time.sleep(2)

    def write(self, xpath: str, text: str):
        time.sleep(2)
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).click().double_click().send_keys(text).perform()
        time.sleep(2)

    def text(self, xpath: str) -> str:
        value = self._driver.find_element(By.XPATH, xpath).get_attribute("value")
        return value

    def download(self, xpath: str) -> str:
        value = self._driver.find_element(By.XPATH, xpath).get_attribute("download")
        return value

    def include(self):
        self._wdw.until(alert_is_present())
        self._driver.switch_to.alert.accept()
        time.sleep(5)

    def login(self):
        self.write('//*[@id="login"]', self._username)
        self.write('//*[@id="password"]', self._password)
        self.click('//*[@id="btn-login"]')

    def close(self):
        self._driver.quit()

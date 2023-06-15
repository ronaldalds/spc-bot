from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import (
    alert_is_present,
)


class Spc:
    def __init__(self, 
                 operation: str, 
                 password: str, 
                 secret: str, 
                 url: str,
                 headless: bool = False
                 ):
        self._operation: str = operation
        self._password: str = password
        self._secret: str = secret
        capabilities = DesiredCapabilities.CHROME.copy()
        largura = 1280
        altura = 960
        options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": "",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
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
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).pause(5).click().pause(5).perform()

    def dbclick(self, xpath: str):
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).pause(5).double_click().pause(5).perform()

    def write(self, xpath: str, text: str):
        self._mouse.move_to_element(self._driver.find_element(
            By.XPATH, xpath
        )).pause(2).click().send_keys(text).pause(2).perform()

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
        self._driver.close()

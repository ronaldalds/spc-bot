from driver.mk.coin.coin import Coin
from driver.mk.aside.aside import Aside
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable,
)


class Mk:
    def __init__(self, username: str, password: str, url: str):
        self._username: str = username
        self._password: str = password
        self._driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self._wdw = WebDriverWait(self._driver, 300)
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

    def minimizeChat(self):
        self._driver.switch_to.default_content()
        self.iframeMain()
        self._wdw.until(element_to_be_clickable(
            (By.XPATH, '//*[@id="jsxc_toggleRoster"]')))
        self._driver.find_element(
            By.XPATH, '//*[@id="jsxc_toggleRoster"]').click()

    def close(self):
        self._driver.close()

    def iframeMain(self):
        self._driver.switch_to.default_content()
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//frame[@name="mainsystem"]')))
        return self

    def iframeForm(self):
        self._driver.switch_to.default_content()
        self.iframeMain()
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//*[@class="FormIframe"]/iframe')))
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))

    def iframeCoin(self):
        self._driver.switch_to.default_content()
        self.iframeMain()
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframeAsideCoin(self, coin: Coin):
        self._driver.switch_to.default_content()
        self.iframeCoin()
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, f'//iframe[@componenteaba="{coin.title()} - PainelCloseAbaPrincipal"]')))
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframePainel(self, coin: Coin, aside: Aside):
        self._driver.switch_to.default_content()
        self.iframeAsideCoin(coin)
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, f'//iframe[@componenteaba="{aside.painel()}ClosePainelAba"]')))
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[@name="mainform"]')))
        return self

    def iframeGrid(self, coin: Coin, aside: Aside):
        self._driver.switch_to.default_content()
        self.iframePainel(coin, aside)
        self._wdw.until(frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//div[@id="lay"]/div[2]/div[2]/div[1]/div/iframe')))
        return self

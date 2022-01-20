import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import fonbet_url

"""

Из полученных данных выбрать любую игру. в Браузере через Selenium открыть игру по названию на сайте fonbet.ru (не по url).
В консоль вывести название выбранной игры.
Использовать Chrome.
"""
# chrome v97


class FonbetSeleParser:

    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(fonbet_url)
        time.sleep(2)

    def open_live_game(self, game_name):
        try:
            search_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="headerContainer"]/div/header/div[2]/div/div[contains(@class, "search")]'))
            )
            time.sleep(0.4)
        except TimeoutException:
            print('page not loaded')
            return None

        search_field = None
        for _ in range(6):
            search_btn.click()
            time.sleep(0.5)
            try:
                search_field = WebDriverWait(self.driver, 3, poll_frequency=0.3).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="search_form"]/div/div/input'))  # """//*[@id="search-component"]/input"""
                )
                break

            except TimeoutException:
                pass

        search_field.send_keys(game_name)

        try:
            game_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-container"]/div[2]/div/div/div[2]/a'))
            )
        except TimeoutException:
            print('game not found')
            return None

        game_link.click()

    def __del__(self):
        try:
            self.driver.close()
            self.driver.quit()
            time.sleep(1)
        except ImportError:
            pass


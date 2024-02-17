import time
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class Search(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    SEARCH_MARKA = ("xpath", "/html/body/div[2]/form/p[2]/select")
    SELECT_MARKA = ("xpath", "/html/body/div[2]/form/p[2]/select/option[5]")     # Mazda
    SEARCH_MODEL = ("xpath", "/html/body/div[2]/form/p[3]/select")
    SELECT_MODEL = ("xpath", "/html/body/div[2]/form/p[3]/select/option[11]")    # 6
    SEARCH_CUZOV = ("xpath", "/html/body/div[2]/form/p[4]/select")
    SELECT_CUZOV = ("xpath", "/html/body/div[2]/form/p[4]/select/option[3]")     # Седан
    EXPLORE_BUTTON = ("xpath", "/html/body/div[2]/form/button")                  # Искать
    CAR_CARD_1 = ("xpath", "/html/body/div[2]/ul/li/a")                          # Карточка авто
    CAR_CARD_2 = ("xpath", "/html/body/div[2]/ul/li[3]/a/img")                   # Карточка авто
    START_PRICE = ("xpath", "/html/body/div[2]/form/p[8]/input")                 # Цена от
    END_PRICE = ("xpath", "/html/body/div[2]/form/p[7]/input")                   # Цена до
    START_MILEAGE = ("xpath", "/html/body/div[2]/form/p[9]/input")               # Пробег от
    END_MILEAGE = ("xpath", "/html/body/div[2]/form/p[10]/input")                # Пробег до
    NEXT_PAGE = ("xpath", "/html/body/nav/ul/li[3]/a")                           # Кнопка следующая страница

    @allure.step("Scroll page to the button")
    def scrol_down_button(self):                                                     # скролл до след. страницы
        nest_page = self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", nest_page)
        # time.sleep(1)

    @allure.step("Click on next page")
    def next_page(self):                                                             # след. страница
        self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE)).click()
        # time.sleep(2)

    @allure.step("Click on search marka")
    def click_search_marka(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MARKA)).click()
        # time.sleep(1)

    @allure.step("Click on select marka")
    def click_select_marka(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MARKA)).click()
        # time.sleep(1)

    @allure.step("Click on search model")
    def click_search_model(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MODEL)).click()
        # time.sleep(1)

    @allure.step("Click on select model")
    def click_select_model(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MODEL)).click()
        # time.sleep(1)

    @allure.step("Click on search cuzov")
    def click_search_cuzov(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_CUZOV)).click()
        # time.sleep(1)

    @allure.step("Click on select cuzov")
    def click_select_cuzov(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CUZOV)).click()
        # time.sleep(1)

    @allure.step("Enter start price")
    def start_price(self, new_price):
        self.wait.until(EC.element_to_be_clickable(self.START_PRICE)).send_keys(new_price)
        # time.sleep(1)

    @allure.step("Enter end price")
    def end_price(self, new_price):
        self.wait.until(EC.element_to_be_clickable(self.END_PRICE)).send_keys(new_price)
        # time.sleep(1)

    @allure.step("Enter start mileage")
    def start_mileage(self, new_mileage):
        self.wait.until(EC.element_to_be_clickable(self.START_MILEAGE)).send_keys(new_mileage)
        # time.sleep(1)

    @allure.step("Enter end mileage")
    def end_mileage(self, new_mileage):
        self.wait.until(EC.element_to_be_clickable(self.END_MILEAGE)).send_keys(new_mileage)
        time.sleep(1)

    @allure.step("Click explore button")
    def explore_search(self):
        self.wait.until(EC.element_to_be_clickable(self.EXPLORE_BUTTON)).click()
        time.sleep(3)

    @allure.step("Click car card 1")
    def car_card_1(self):
        self.wait.until(EC.element_to_be_clickable(self.CAR_CARD_1)).click()
        # time.sleep(2)

    @allure.step("Click car card 2")
    def car_card_2(self):
        self.wait.until(EC.element_to_be_clickable(self.CAR_CARD_2)).click()
        # time.sleep(2)


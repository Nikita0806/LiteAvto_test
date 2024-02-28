import os
import time
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OfferPage(BasePage):
    PAGE_URL = Links.OFFER_PAGE

    SEARCH_MARKA = ("xpath", '//*[@id="id_marka"]')  # Выбор списка
    SELECT_MARKA = ("xpath", '//*[@id="id_marka"]/option[2]')  # Выбор в списке
    SEARCH_MODEL = ("xpath", '//*[@id="id_model"]')
    SELECT_MODEL = ("xpath", '//*[@id="id_model"]/option[2]')  # Camry
    SEARCH_CUZOV = ("xpath", '//*[@id="id_cuzov"]')
    SELECT_CUZOV = ("xpath", '//*[@id="id_cuzov"]/option[3]')  # Седан
    COLOR = ("xpath", '//*[@id="id_cvet"]')  # Цвет
    VIN = ("xpath", '//*[@id="id_vin"]')  # VIN
    EQUIPMENT = ("xpath", '//*[@id="id_compl"]')  # Комплектация
    SEARCH_DATE = ("xpath", '//*[@id="id_data"]')
    SELECT_DATE = ("xpath", '/html/body/form/div/p[7]/select/option[31]')  # Год выпуска
    PRICE = ("xpath", '//*[@id="id_price"]')  # Цена
    MILEAGE = ("xpath", '//*[@id="id_probeg"]')  # Пробег
    SEARCH_TRANSMISSION = ("xpath", '//*[@id="id_trans"]')
    SELECT_TRANSMISSION = ("xpath", '//*[@id="id_trans"]/option[2]')  # Трансмиссия
    SEARCH_ENGINE_CAPACITY = ("xpath", '//*[@id="id_obem"]')
    SELECT_ENGINE_CAPACITY = ("xpath", '//*[@id="id_obem"]/option[22]')  # Объём двигателя
    SEARCH_ENGINE_TYPE = ("xpath", '//*[@id="id_top"]')
    SELECT_ENGINE_TYPE = ("xpath", '//*[@id="id_top"]/option[2]')  # Тип двигателя
    SEARCH_DRIVE_UNIT = ("xpath", '//*[@id="id_priv"]')
    SELECT_DRIVE_UNIT = ("xpath", '//*[@id="id_priv"]/option[3]')  # Привод
    SEARCH_STATE = ("xpath", '//*[@id="id_sost"]')
    SELECT_STATE = ("xpath", '//*[@id="id_sost"]/option[2]')  # Состояние
    HORSEPOWER = ("xpath", '//*[@id="id_ls"]')  # Лошадиные силы
    SEARCH_PTS = ("xpath", '//*[@id="id_pts"]')
    SELECT_PTS = ("xpath", '//*[@id="id_pts"]/option[3]')  # ПТС
    OWNERS = ("xpath", '//*[@id="id_vlad"]')  # Владельцы
    SEARCH_ACCOUNTING = ("xpath", '//*[@id="id_uchet"]')
    SELECT_ACCOUNTING = ("xpath", '//*[@id="id_uchet"]/option[2]')  # Учет
    TELEPHONE = ("xpath", '//*[@id="id_tel"]')  # Телефон
    DESCRIPTION = ("xpath", '//*[@id="id_opis"]')  # Описание
    SAVE_BUTTON = ("xpath", '/html/body/form/div/button')
    PHOTO1 = ("xpath", '//*[@id="id_photo1"]')
    PHOTO2 = ("xpath", '//*[@id="id_photo2"]')
    PHOTO3 = ("xpath", '//*[@id="id_photo3"]')

    @allure.step("Scroll page to the button")
    def scrol_save_button(self):
        ave_button = self.driver.find_element(By.XPATH, '/html/body/form/div/button')
        self.driver.execute_script("arguments[0].scrollIntoView();", ave_button)
        # time.sleep(1)

        # Выбор марки

    @allure.step("Click on search marka")
    def click_search_marka(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MARKA)).click()
        # time.sleep(1)

    @allure.step("Click on select marka")
    def click_select_marka(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MARKA)).click()
        # time.sleep(1)

        # Выбор модели

    @allure.step("Click on search model")
    def click_search_model(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MODEL)).click()
        # time.sleep(1)

    @allure.step("Click on select model")
    def click_select_model(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MODEL)).click()
        # time.sleep(1)

        # Выбор кузова

    @allure.step("Click on search cuzov")
    def click_search_cuzov(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_CUZOV)).click()
        # time.sleep(1)

    @allure.step("Click on select cuzov")
    def click_select_cuzov(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CUZOV)).click()
        # time.sleep(1)

        # Ввод цвета

    @allure.step("Enter on color")
    def enter_color(self, color):
        self.wait.until(EC.element_to_be_clickable(self.COLOR)).send_keys(color)
        # time.sleep(1)

        # Ввод VIN

    @allure.step("Enter on vin")
    def enter_vin(self, vin):
        self.wait.until(EC.element_to_be_clickable(self.VIN)).send_keys(vin)
        # time.sleep(1)

        # Комплектация

    @allure.step("Enter on equipment")
    def enter_equipment(self, equipment):
        self.wait.until(EC.element_to_be_clickable(self.EQUIPMENT)).send_keys(equipment)
        # time.sleep(1)

        # Выбор даты

    @allure.step("Click on search date")
    def click_search_date(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_DATE)).click()
        # time.sleep(1)

    @allure.step("Click on select date")
    def click_select_date(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DATE)).click()
        # time.sleep(1)

        # Ввод цены

    @allure.step("Enter on price")
    def enter_price(self, price):
        self.wait.until(EC.element_to_be_clickable(self.PRICE)).send_keys(price)
        # time.sleep(1)

        # Пробег

    @allure.step("Enter on mileage")
    def enter_mileage(self, mileage):
        self.wait.until(EC.element_to_be_clickable(self.MILEAGE)).send_keys(mileage)
        # time.sleep(1)

        # Выбор трансмиссии

    @allure.step("Click on search transmission")
    def click_search_transmission(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_TRANSMISSION)).click()
        # time.sleep(1)

    @allure.step("Click on select transmission")
    def click_select_transmission(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_TRANSMISSION)).click()
        # time.sleep(1)

        # Выбор объём двигателя

    @allure.step("Click on search engine capacity")
    def click_search_engine_capacity(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_ENGINE_CAPACITY)).click()
        # time.sleep(1)

    @allure.step("Click on select engine capacity")
    def click_select_engine_capacity(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ENGINE_CAPACITY)).click()
        # time.sleep(1)

        # Выбор тип двигателя

    @allure.step("Click on search engine type")
    def click_search_engine_type(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_ENGINE_TYPE)).click()
        # time.sleep(1)

    @allure.step("Click on select engine type")
    def click_select_engine_type(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ENGINE_TYPE)).click()
        # time.sleep(1)

        # Выбор привода

    @allure.step("Click on search drive unit")
    def click_search_drive_unit(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_DRIVE_UNIT)).click()
        # time.sleep(1)

    @allure.step("Click on select drive unit")
    def click_select_drive_unit(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DRIVE_UNIT)).click()
        # time.sleep(1)

        # Выбор состояния

    @allure.step("Click on search state")
    def click_search_state(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_STATE)).click()
        # time.sleep(1)

    @allure.step("Click on select state")
    def click_select_state(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_STATE)).click()
        # time.sleep(1)

        # Лошадиные силы

    @allure.step("Enter on horsepower")
    def enter_horsepower(self, horsepower):
        self.wait.until(EC.element_to_be_clickable(self.HORSEPOWER)).send_keys(horsepower)
        # time.sleep(1)

        # Выбор ПТС

    @allure.step("Click on search pts")
    def click_search_pts(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_PTS)).click()
        # time.sleep(1)

    @allure.step("Click on select pts")
    def click_select_pts(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_PTS)).click()
        # time.sleep(1)

        # Владельцы

    @allure.step("Enter on owners")
    def enter_owners(self, owners):
        self.wait.until(EC.element_to_be_clickable(self.OWNERS)).send_keys(owners)
        # time.sleep(1)

        # Выбор учета

    @allure.step("Click on search accounting")
    def click_search_accounting(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_ACCOUNTING)).click()
        # time.sleep(1)

    @allure.step("Click on select accounting")
    def click_select_accounting(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ACCOUNTING)).click()
        # time.sleep(1)

        # Телефон

    @allure.step("Enter on telephone")
    def enter_telephone(self, telephone):
        self.wait.until(EC.element_to_be_clickable(self.TELEPHONE)).send_keys(telephone)
        # time.sleep(1)

        # фото1
    @allure.step("Enter on photo 1")

    def photo_1(self):
        self.wait.until(EC.element_to_be_clickable(self.PHOTO1)).send_keys(f"{os.getcwd()}/photo/1.webp")
        # time.sleep(1)

        # фото2
    @allure.step("Enter on photo 2")
    def photo_2(self):
        self.wait.until(EC.element_to_be_clickable(self.PHOTO2)).send_keys(f"{os.getcwd()}/photo/2.webp")
        time.sleep(1)

        # фото3
    @allure.step("Enter on photo 3")
    def photo_3(self):
        self.wait.until(EC.element_to_be_clickable(self.PHOTO3)).send_keys(f"{os.getcwd()}/photo/3.webp")
        time.sleep(1)

        # Описание

    @allure.step("Enter on description")
    def enter_description(self, description):
        self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION)).send_keys(description)
        # time.sleep(1)

        # Сохранение

    @allure.step("Click on save button")
    def save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(2)

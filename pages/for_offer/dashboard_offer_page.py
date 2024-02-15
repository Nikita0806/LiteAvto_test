import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardOfferPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    LOGIN_BATTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[2]")         # логин
    ADD_CAR_BUTTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[1]")   # предложить автомобиль

    @allure.step("Click on login")
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BATTON)).click()
        # time.sleep(2)

    @allure.step("Click on add car")
    def click_offer(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_CAR_BUTTON)).click()
        time.sleep(1)
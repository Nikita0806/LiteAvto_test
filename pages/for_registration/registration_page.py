import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):

    PAGE_URL = Links.REGISTRATION_PAGE

    USERNAME_FIELD = ("xpath", "/html/body/form/div/p[2]/input")
    PASSWORD_FIELD = ("xpath", "/html/body/form/div/p[3]/input")
    REPEAT_PASSWORD_FIELD = ("xpath", "/html/body/form/div/p[4]/input")
    SUBMIT_BUTTON = ("xpath", "/html/body/form/div/button")
    EXIT_LOGIN = ("xpath", '//*[@id="mainmenu"]/li[5]/a[2]')

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
        # time.sleep(2)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)

    @allure.step("Enter repeat password")
    def enter_repeat_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.REPEAT_PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        time.sleep(5)

    @allure.step("Click exit login")
    def exit_login(self):
        self.wait.until(EC.element_to_be_clickable(self.EXIT_LOGIN)).click()
        # time.sleep(2)

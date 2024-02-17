# import random
#
# import allure
# import pytest
# from base.base_test import BaseTest
#
#
# @allure.feature("Registration")
# class TestRegistration(BaseTest):
#
#     @allure.title("Registration")
#     @allure.severity("Medium")
#     @pytest.mark.registration
#     def test_registration(self):
#         self.dashboard_registration_page.open()
#         self.dashboard_registration_page.is_opened()                                # проверка открытия страницы
#         self.dashboard_registration_page.click_registration()                       # нажатие кнопки
#         self.registration_page.open()                                               # открытие страницы
#         self.registration_page.enter_login(f"Никита{random.randint(1, 100000)}")                      # ввод логина
#         self.registration_page.enter_password(self.data.R_PASSWORD)                 # ввод пароля
#         self.registration_page.enter_repeat_password(self.data.R_REPEAT_PASSWORD)
#         self.registration_page.click_submit_button()                                # нажатие на кнопку
#         self.dashboard_registration_page.make_screenshot("Enter registration")



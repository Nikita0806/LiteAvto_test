# import allure
# import pytest
# from base.base_test import BaseTest


# @allure.feature("Login")
# class TestLogin(BaseTest):

#     @allure.title("Login")
#     @allure.severity("Medium")
#     @pytest.mark.login
#     def test_login(self):
#         self.dashboard_login_page.open()                    # открытие страницы
#         self.dashboard_login_page.is_opened()               # проверка открытия страницы
#         self.dashboard_login_page.click_login()             # нажатие кнопки
#         self.login_page.open()                              # открытие страницы
#         self.login_page.enter_login(self.data.LOGIN)        # ввод логина
#         self.login_page.enter_password(self.data.PASSWORD)  # ввод пароля
#         self.login_page.click_submit_button()               # нажатие на кнопку
#         self.login_page.make_screenshot("Screenshot login")

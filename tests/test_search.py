# import random
# import allure
# import pytest
# from base.base_test import BaseTest
#
#
# @allure.feature("Search test")
# class TestSearch(BaseTest):
#
#     @allure.title("Search")
#     @allure.severity("Medium")
#     @pytest.mark.search
#     def test_search(self):
#         self.dashboard_login_page.open()                    # открытие страницы
#         self.dashboard_login_page.is_opened()               # проверка открытия страницы
#         self.dashboard_login_page.click_login()             # нажатие кнопки
#         self.login_page.open()                              # открытие страницы
#         self.login_page.enter_login(self.data.LOGIN)        # ввод логина
#         self.login_page.enter_password(self.data.PASSWORD)  # ввод пароля
#         self.login_page.click_submit_button()               # нажатие на кнопку
#         self.search.open()
#         self.search.is_opened()
#         self.search.scrol_down_button()
#         self.search.next_page()
#         self.search.scrol_down()
#         self.search.scrol_up()
#         self.search.click_search_marka()
#         self.search.click_select_marka()
#         self.search.enter_select_marka()                        # Проверяет, написано ли мазда
        # self.search.click_search_model()
        # self.search.click_select_model()
        # self.search.click_search_cuzov()
        # self.search.click_select_cuzov()
        # self.search.start_price(f"26{random.randint(100, 1000)}")
        # self.search.end_price(f"3{random.randint(50000, 5000000)}")
        # self.search.start_mileage(f"46{random.randint(10, 1000)}")
        # self.search.end_mileage(f"5{random.randint(50000, 60000)}")
        # self.search.explore_search()
        # self.search.car_card_1()
        # self.search.scrol_down()
        # self.search.scrol_up()
        # self.search.make_screenshot("Screenshot new car card")


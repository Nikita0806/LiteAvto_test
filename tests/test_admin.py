# import allure
# import pytest
# from base.base_test import BaseTest


# @allure.feature("Adding a car to the page")
# class TestAdminCar(BaseTest):

#     @allure.title("Admin")
#     @allure.severity("Medium")
#     @pytest.mark.admin
#     def test_admin(self):
#         # host
#         self.search.open()                                      # открытие страницы
#         self.search.scrol_down_button()                         # скролл до кнопки
#         self.search.next_page()                                 # Следующая страница
#         # admin
#         self.admin_page.open()                                  # открыте админки
#         self.admin_page.enter_login(self.data.LOGIN)            # ввод логина
#         self.admin_page.enter_password(self.data.PASSWORD)      # ввод пароля
#         self.admin_page.click_submit_button()                   # вход
#         self.admin_page.car_button()                            # выбор атомобили
#         # self.admin_page.checkbox_click_settings_on_1()          # вкл чекбокс настроек
#         # self.admin_page.click_settings_select()                 # выбор выпадающего списка настроек
#         # self.admin_page.click_settings()                        # выбор настроек
#         # self.admin_page.click_settings_button()                 # Выполнение настроек
#         # self.admin_page.click_settings_button_agreement()       # Подтверждение настроек
#         self.admin_page.checkbox_click_on()                     # вкл чекбокса в продаже
#         self.admin_page.checkbox_click_off()                    # выкл чекбокса в продаже
#         self.admin_page.scrol_down()                            # скролл вниз
#         self.admin_page.save_button()                           # сохранить
#         # host
#         self.search.open()                                      # открытие страницы
#         self.search.scrol_down_button()                         # скролл до кнопки
#         self.search.next_page()                                 # Следующая страница
#         self.admin_page.make_screenshot("Screenshot new car")

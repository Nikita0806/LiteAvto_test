import pytest
from config.data import Data
from pages.for_login.login_page import LoginPage
from pages.for_registration.registration_page import RegistrationPage
from pages.for_login.dashboard_login_page import DashboardLoginPage
from pages.for_registration.dashboard_registration_page import DashboardRegistrationPage
from pages.for_search.dashborad_search_page import Search
from pages.for_offer.dashboard_offer_page import DashboardOfferPage
from pages.for_offer.offer_page import OfferPage
from pages.for_admin.admin_page import AdminPage

class BaseTest:                             # базовый для наших тестов для инотации типов

    data: Data                              # из данных (пароли)

    login_page: LoginPage                   # аннотация
    registration_page: RegistrationPage
    dashboard_login_page: DashboardLoginPage
    dashboard_registration_page: DashboardRegistrationPage
    search: Search
    dashboard_offer_page: DashboardOfferPage
    offer_page: OfferPage
    admin_page: AdminPage

    @pytest.fixture(autouse=True)           # autouse=True для всех тестов она применяется
    def setup(self, request, driver):       # фикстура
        request.cls.driver = driver         # чтобы в тестах могли использовать драйвер
        request.cls.data = Data()           # чтобы в тестах могли использовать пароли
        request.cls.login_page = LoginPage(driver)          # объекты страниц
        request.cls.registration_page = RegistrationPage(driver)
        request.cls.dashboard_login_page = DashboardLoginPage(driver)
        request.cls.dashboard_registration_page = DashboardRegistrationPage(driver)
        request.cls.search = Search(driver)
        request.cls.dashboard_offer_page = DashboardOfferPage(driver)
        request.cls.offer_page = OfferPage(driver)
        request.cls.admin_page = AdminPage(driver)

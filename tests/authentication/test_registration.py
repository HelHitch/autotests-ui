import allure
import pytest
from allure_commons.types import Severity

from pages.authentication.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    @allure.severity(Severity.BLOCKER)
    @allure.title("Registration with correct email, username and password")
    def test_successful_registration(self, registration_page: RegistrationPage,
                                     dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_page.registration_form.check_visible()
        registration_page.registration_form.fill(email="user.name@gmail.com",
                                                 login="username",
                                                 password="password")
        registration_page.registration_form.check_visible(email="user.name@gmail.com",
                                                         login="username",
                                                         password="password")
        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()

    @allure.severity(Severity.NORMAL)
    @allure.title("Navigation from registration page to login page")
    def test_navigate_from_registration_to_authorization(self,
                                                         registration_page: RegistrationPage,
                                                         login_page: LoginPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.click_login_link()
        login_page.login_form.check_visible()
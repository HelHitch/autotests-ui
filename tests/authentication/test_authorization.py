import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
class TestAuthorization:
    @pytest.mark.login
    @pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"),
                                                   ("user.name@gmail.com", "  "),
                                                   ("  ", "password")],
                             ids=["Проверяем, что пользователь не может войти в систему с невалидными email и password",
                                  "Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password",
                                  "Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password"])
    def test_wrong_email_or_password_authorization(self, email: str, password: str, login_page: LoginPage):  # Создаем тестовую функцию

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.login_form.check_visible()
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(self,
                                      registration_page:RegistrationPage,
                                      login_page: LoginPage,
                                      dashboard_page: DashboardPage):

        registration_page.visit(url="https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(
            email="user@mail.ru",
            login="user",
            password="pwd"
        )
        registration_page.click_registration_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible(username="user")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="user@mail.ru", password="pwd")
        login_page.login_btn.click()

        dashboard_page.navbar.check_visible(username="user")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()


    def test_navigate_from_authorization_to_registration(self,
                                          registration_page:RegistrationPage,
                                          login_page: LoginPage):

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.registration_form.check_visible()



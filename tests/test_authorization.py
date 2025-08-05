import pytest
from playwright.sync_api import expect, sync_playwright

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [("user.name@gmail.com", "password"),
                                               ("user.name@gmail.com", "  "),
                                               ("  ", "password")],
                         ids=["Проверяем, что пользователь не может войти в систему с невалидными email и password",
                              "Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password",
                              "Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password"])
def test_wrong_email_or_password_authorization(email: str, password: str, login_page: LoginPage):  # Создаем тестовую функцию

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.login_form.check_visible()
    login_page.login_form.fill(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()



import time

import pytest
from playwright.sync_api import expect, sync_playwright

@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [("user.name@gmail.com", "password"),
                                               ("user.name@gmail.com", "  "),
                                               ("  ", "password")],
                         ids=["Проверяем, что пользователь не может войти в систему с невалидными email и password",
                              "Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password",
                              "Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password"])
def test_wrong_email_or_password_authorization(email: str, password: str):  # Создаем тестовую функцию
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        login_button = page.get_by_test_id('login-page-login-button')
        time.sleep(5)
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")


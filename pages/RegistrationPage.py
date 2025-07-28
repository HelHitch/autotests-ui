from playwright.sync_api import Page, expect

from pages.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)
        self.email_input = page.get_by_test_id("registration-form-email-input").locator("//input")
        self.login_input = page.get_by_test_id("registration-form-username-input").locator("//input")
        self.pwd_input = page.get_by_test_id("registration-form-password-input").locator("//input")
        self.btn = page.get_by_test_id("registration-page-registration-button")


    def fill_registration_form(self, email:str, login:str, password:str):

        self.email_input.fill(value=email)
        self.page.screenshot(path='./new.png')
        expect(self.email_input).to_have_value(email)

        self.login_input.fill(value=login)
        expect(self.login_input).to_have_value(login)

        self.pwd_input.fill(password)
        expect(self.pwd_input).to_have_value(password)

    def click_registration_button(self):
        self.btn.click()




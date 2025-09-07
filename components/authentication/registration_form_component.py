from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(
            page=page,
            locator="registration-form-email-input",
            name="Registration Email input"
        )
        self.login_input = Input(
            page=page,
            locator="registration-form-username-input",
            name="Registration Login Input"
        )
        self.password_input =  Input(page=page,
                                     locator="registration-form-password-input",
                                     name="Registration Password Input")

    def fill(self, email:str, login:str, password:str):
        self.email_input.fill(value=email)
        self.login_input.fill(value=login)
        self.password_input.fill(value=password)

    def check_visible(self, email:str='', login:str='', password:str=''):
        self.email_input.check_visible()
        self.email_input.check_have_value(value=email)

        self.login_input.check_visible()
        self.login_input.check_have_value(value=login)

        self.password_input.check_visible()
        self.password_input.check_have_value(value=password)



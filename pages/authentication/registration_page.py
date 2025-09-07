import re

import pytest
from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage

@pytest.mark.regression
@pytest.mark.registration
class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)
        self.registration_form = RegistrationFormComponent(page=page)
        self.btn = Button(page=page,
                          locator="registration-page-registration-button",
                          name="Registration Button")
        self.login_link = Link(page=page,
                          locator="registration-page-login-link",
                          name="Login")

    def click_registration_button(self):
        self.btn.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(expected_url=re.compile(".*/#/auth/registration"))




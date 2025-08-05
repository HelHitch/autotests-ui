from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)
        self.registration_form = RegistrationFormComponent(page=page)
        self.btn = page.get_by_test_id("registration-page-registration-button")

    def click_registration_button(self):
        self.btn.click()




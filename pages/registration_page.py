from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)
        self.registration_form = RegistrationFormComponent(page=page)
        self.btn = Button(page=page,
                          locator="registration-page-registration-button",
                          name="Registration Button")

    def click_registration_button(self):
        self.btn.click()




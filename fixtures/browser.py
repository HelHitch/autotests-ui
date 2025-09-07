import json

import pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def initialize_browser_state(playwright: Playwright, registration_page:RegistrationPage) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    new_page = context.new_page()

    reg_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    new_page.goto(reg_url)
    registration_page.registration_form.fill(email="user.name@gmail.com",
                                             login="username",
                                             password="password")

    registration_page.click_registration_button()

    with open('auth_data.json', 'w+') as auth_data:
        auth_data.write(json.dumps(context.storage_state()))
    yield new_page


@pytest.fixture(scope='function')
def chromium_page_with_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()

    with open('auth_data.json', 'r') as auth_data:
        storage_state = json.loads(auth_data.read())

    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    yield page
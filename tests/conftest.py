import json

import pytest
from playwright.sync_api import Page, Playwright
from pytest_playwright.pytest_playwright import playwright



@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    new_page = context.new_page()

    reg_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    new_page.goto(reg_url)

    email_input = new_page.get_by_test_id("registration-form-email-input").locator("//input")
    login_input = new_page.get_by_test_id("registration-form-username-input").locator("//input")
    pwd_input = new_page.get_by_test_id("registration-form-password-input").locator("//input")
    btn = new_page.get_by_test_id("registration-page-registration-button")


    email_input.fill("user.name@gmail.com")
    login_input.fill("username")
    pwd_input.fill("password")
    btn.click()

    with open('auth_data.json', 'w+') as auth_data:
        auth_data.write(json.dumps(context.storage_state()))




@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)

    with open('auth_data.json', 'r') as auth_data:
        storage_state = json.loads(auth_data.read())

    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    yield page
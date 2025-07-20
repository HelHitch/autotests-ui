import json

from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
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
        auth_data.seek(0)
        storage_state = json.loads(auth_data.read())


    context2 = browser.new_context(storage_state=storage_state)
    context_new_page = context2.new_page()
    context_new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = new_page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_have_text(expected="Courses")

    no_result_text = new_page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_result_text).to_have_text(expected="There is no results")
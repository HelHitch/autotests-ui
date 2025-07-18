from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:


    browser = p.chromium.launch(headless=False)
    new_page = browser.new_page()

    reg_url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    new_page.goto(reg_url)

    btn = new_page.get_by_test_id("registration-page-registration-button")
    expect(btn).to_be_disabled()


    email_input = new_page.get_by_test_id("registration-form-email-input").locator("//input")
    login_input = new_page.get_by_test_id("registration-form-username-input").locator("//input")
    pwd_input = new_page.get_by_test_id("registration-form-password-input").locator("//input")
    email_input.fill("user.name@gmail.com")
    login_input.fill("username")
    pwd_input.fill("password")

    expect(btn).to_be_enabled()

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:


    browser = p.chromium.launch(headless=False)
    new_page = browser.new_page()

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

    graph_title = new_page.get_by_test_id("dashboard-toolbar-title-text")
    expect(graph_title).to_have_text(expected="Dashboard")

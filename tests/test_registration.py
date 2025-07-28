


def test_successful_registration(registration_page,
                                 dashboard_page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.fill_registration_form(email="user.name@gmail.com",
                                             login="username",
                                             password="password")
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
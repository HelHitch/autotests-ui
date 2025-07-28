import pytest
from playwright.sync_api import Page

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.RegistrationPage import RegistrationPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page=page)

@pytest.fixture
def registration_page(page: Page):
    return RegistrationPage(page=page)

@pytest.fixture
def dashboard_page(page: Page):
    return DashboardPage(page=page)
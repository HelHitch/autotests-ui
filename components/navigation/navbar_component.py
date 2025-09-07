from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page=page,
                              locator='navigation-navbar-app-title-text',
                              name="App Title")
        self.welcome_title = Text(page=page,
                              locator='navigation-navbar-welcome-title-text',
                              name="Welcome Title")

    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_text(expected_text='UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_text(expected_text=f'Welcome, {username}!')
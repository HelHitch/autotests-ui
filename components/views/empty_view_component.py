

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier=identifier
        self.icon = Icon(page=page,
                         locator="{identifier}-empty-view-icon",
                         name="Empty View Icon")
        self.title = Text(page=page,
                          locator="{identifier}-empty-view-title-text",
                          name="Empty View Title")
        self.description = Text(page=page,
                                locator="{identifier}-empty-view-description-text",
                                name="Empty View Description")

    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        self.icon.check_visible(identifier=self.identifier)

        # Проверяем видимость заголовка и его текст
        self.title.check_visible(identifier=self.identifier)
        self.title.check_text(expected_text=title, identifier=self.identifier)

        # Проверяем видимость описания и его текст
        self.description.check_visible(identifier=self.identifier)
        self.description.check_text(expected_text=description,
                                    identifier=self.identifier)
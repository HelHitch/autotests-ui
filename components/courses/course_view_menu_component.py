from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page=page,
                                  locator='course-view-menu-button',
                                  name="Course Menu Button")
        self.edit_menu_item = Button(page=page,
                                     locator='course-view-edit-menu-item',
                                     name="Edit Course Button")
        self.delete_menu_item = Button(page=page,
                                locator= 'course-view-delete-menu-item',
                                name="Edit Course Button")

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)
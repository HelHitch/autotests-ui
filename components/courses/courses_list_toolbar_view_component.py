import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page=page,
                          locator='courses-list-toolbar-title-text',
                          name="Course List Title")
        self.create_course_button = Button(page=page,
                                           locator='courses-list-toolbar-create-course-button',
                                           name="Create Course Button")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_text(expected_text='Courses')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses/create"))
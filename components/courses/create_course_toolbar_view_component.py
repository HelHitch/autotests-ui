from playwright.sync_api import Page
from components.base_component import BaseComponent, expect
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page=page,
                                        locator='create-course-toolbar-title-text',
                                        name="Create Course Title")
        self.create_course_button = Button(page=page,
                                           locator="create-course-toolbar-create-course-button",
                                           name="Create Course Button")

    def check_visible(self, is_create_course_disabled:bool = False):
        self.create_course_title.check_visible()
        self.create_course_title.check_text(expected_text='Create course')

        self.create_course_button.check_visible()
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()


    def click_create_course_button(self):
        self.create_course_button.click()
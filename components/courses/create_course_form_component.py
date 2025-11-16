import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent, expect
from elements.button import Button
from elements.input import Input
from elements.text import Text
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page=page,
                                        locator="create-course-toolbar-title-text",
                                        name="Create Course List")
        self.create_course_button = Button(page=page,
                                           locator="create-course-toolbar-create-course-button",
                                           name="Create Course Button")

        self.create_course_title_input = Input(page=page,
                                               locator="create-course-form-title-input",
                                               name="Course Title Input")
        self.create_course_estimated_time_input = Input(page=page, locator="create-course-form-estimated-time-input",
                                                        name="Estimated Time Input")
        self.create_course_description_textarea = Textarea(page=page, locator="create-course-form-description-input",
                                                        name="Course Description Input")
        self.create_course_max_score_input = Input(page=page,
                                                   locator="create-course-form-max-score-input",
                                                   name="Create Course Max Score")
        self.create_course_min_score_input = Input(page=page,
                                                  locator="create-course-form-min-score-input",
                                                  name="Create Course Min Score")

    @allure.step("Check course creation form is visible")
    def check_visible(self,
                      title: str,
                      estimated_time: str,
                      description: str,
                      max_score: str,
                      min_score: str):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_text(expected_text=title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(value=estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(value=description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(value=max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(value=min_score)

    @allure.step("Fill course main data")
    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):

        self.create_course_title_input.fill(title)
        self.create_course_title_input.check_have_value(value=title)

        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_estimated_time_input.check_have_value(value=estimated_time)

        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea.check_have_value(value=description)

        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input.check_have_value(value=max_score)

        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input.check_have_value(value=min_score)
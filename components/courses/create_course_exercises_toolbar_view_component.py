import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(page=page,
                                    locator="create-course-exercises-box-toolbar-title-text",
                                    name="Exercise Title")
        self.create_exercise_button = Button(page=page,
                                             locator="create-course-exercises-box-toolbar-create-exercise-button",
                                             name="Create Excessive Button")

    @allure.step("Check courses exercises tool bar is visible")
    def check_visible(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_text(expected_text='Exercises')
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
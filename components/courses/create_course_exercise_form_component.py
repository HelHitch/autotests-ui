from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):

    def __init__(self, page:Page):
        super().__init__(page=page)
        self.delete_exercise_button = Button(
            page=page,
            locator="create-course-exercise-{index}-box-toolbar-delete-exercise-button",
            name="Delete Exercise"
        )
        self.subtitle = Text(page=page,
                        locator="create-course-exercise-{index}-box-toolbar-subtitle-text",
                        name="Exercise Subtitle")
        self.title_input = Input(page=page,
                            locator="create-course-exercise-form-title-{index}-input",
                            name="Title")
        self.description_input = Input(page=page,
                                  locator="create-course-exercise-form-description-{index}-input",
                                  name="Description")


    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible(index=index)
        self.subtitle.check_text(expected_text=f"#{index + 1} Exercise", index=index)

        self.title_input.check_visible()
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(value=description, index=index)

    def fill(self, index: int, title: str, description: str):
        self.title_input.fill(value=title, index=index)
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.fill(value=description, index=index)
        self.description_input.check_have_value(value=description, index=index)
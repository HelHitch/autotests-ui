from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page=page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page=page,
                                                       identifier='create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page=page)
        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page=page)
        self.create_course_form = CreateCourseFormComponent(page=page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page=page)


    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(title='There is no exercises',
                                                description='Click on "Create exercise" button to create new exercise')

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

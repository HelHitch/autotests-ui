import os
import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar.check_visible()
        courses_list_page.check_visible_empty_view()


    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)


        create_course_page.create_course_form.check_visible(
            title='',
            description='',
            estimated_time='',
            min_score='0',
            max_score='0'
        )

        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        file_path = os.path.join('..', 'testdata', 'files', 'image.jpeg')
        create_course_page.image_upload_widget.upload_preview_image(file=file_path)

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_form.create_course_button.click()

        # Переход на страницу курсов
        courses_list_page.toolbar.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    def test_edit_course(self,
                         courses_list_page: CoursesListPage,
                         create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Заполняем форму
        file_path = os.path.join('.', 'testdata', 'files', 'image.jpeg')
        create_course_page.image_upload_widget.upload_preview_image(file=file_path)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            description="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )
        # Сохраняем форму
        create_course_page.create_course_form.create_course_button.click()

        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

        # Редактируем форму
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title="",
            description="",
            estimated_time="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_course_form.fill(
            title="Abracadabra",
            description="Abra ulala",
            estimated_time="3 min",
            max_score="3",
            min_score="1"
        )
        create_course_page.create_course_form.create_course_button.click()
        # Проверяем изменения
        courses_list_page.course_view.check_visible(
            index=0,
            title="Abracadabra",
            estimated_time="3 min",
            max_score="3",
            min_score="1"
        )




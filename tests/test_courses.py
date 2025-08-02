import os
from operator import index

import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_have_text(expected="Courses")

    no_result_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_result_text).to_have_text(expected="There is no results")

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page, create_course_page):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()

    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)


    create_course_page.check_visible_create_course_form(
        title='',
        description='',
        estimated_time='',
        min_score='0',
        max_score='0'
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    file_path = os.path.join('.', 'testdata', 'files', 'image.jpeg')
    create_course_page.upload_preview_image(file=file_path)

    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    course_data = {'title':"Playwright",
                  'estimated_time':"2 weeks",
                  'description':"Playwright",
                  'max_score':"100",
                  'min_score':"10"}

    create_course_page.fill_create_course_form(
        title=course_data['title'],
        estimated_time=course_data['estimated_time'],
        description=course_data['description'],
        max_score=course_data['max_score'],
        min_score=course_data['min_score']
    )
    create_course_page.click_create_course_button()

    # Переход на страницу курсов
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title=course_data['title'],
        estimated_time=course_data['estimated_time'],
        max_score=course_data['max_score'],
        min_score=course_data['min_score']
    )



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
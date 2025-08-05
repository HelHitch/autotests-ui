from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)
        self.navbar = NavbarComponent(page)
        self.toolbar = CoursesListToolbarViewComponent(page)
        self.sidebar = SidebarComponent(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')


    def check_visible_empty_view(self):
        self.empty_view.check_visible(title='There is no results',
                                      description='Results from the load test pipeline will be displayed here')
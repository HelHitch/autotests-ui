from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)
        self.title = Text(page=page,
                          locator='course-widget-title-text',
                          name="Course Title")
        self.image = Image(page=page,
                           locator='course-preview-image',
                           name="Course Image")
        self.max_score_text =  Text(page=page,
                                    locator='course-max-score-info-row-view-text',
                                    name="Course Max Score")
        self.min_score_text = Text(page=page,
                                     locator='course-min-score-info-row-view-text',
                                     name="Course Min Score")
        self.estimated_time_text = Text(page=page,
                                        locator='course-estimated-time-info-row-view-text',
                                        name="Course Estimated Time")

    def check_visible(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.check_text(nth=index, expected_text=title)

        self.max_score_text.check_visible(nth=index)
        self.max_score_text.check_text(nth=index, expected_text=f"Max score: {max_score}")

        self.min_score_text.check_visible(nth=index)
        self.min_score_text.check_text(nth=index, expected_text=f"Min score: {min_score}")

        self.estimated_time_text.check_visible(nth=index)
        self.estimated_time_text.check_text(nth=index, expected_text=f"Estimated time: {estimated_time}")
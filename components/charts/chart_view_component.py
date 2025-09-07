from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    """
    Args:
        identifier: students, activities, courses, scores
        chart_type: bar, line, pie, scatter
    """
    def __init__(self, page: Page, identifier:str , chart_type:str ):
        super().__init__(page)

        self.chart_title = Text(page=page,
                                locator=f'{identifier}-widget-title-text',
                                name="Chart title")
        self.chart_type = Image(page=page,
                                locator=f'{identifier}-{chart_type}-chart',
                                name = "Chart")


    def check_visible(self, title:str):
        self.chart_title.check_visible()
        self.chart_title.check_text(expected_text=title)

        self.chart_type.check_visible()

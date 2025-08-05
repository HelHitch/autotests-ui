from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    """
    Args:
        identifier: students, activities, courses, scores
        chart_type: bar, line, pie, scatter
    """
    def __init__(self, page: Page, identifier:str , chart_type:str ):
        super().__init__(page)

        self.chart_title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart_type = page.get_by_test_id(f'{identifier}-{chart_type}-chart')


    def check_visible(self):
        expect(self.chart_title).to_be_visible()
        expect(self.chart_type).to_be_visible()

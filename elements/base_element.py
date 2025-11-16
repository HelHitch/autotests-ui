import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Args:
        page: Page
        locator: Локатор элемента
        name: строка для форматирования локатора при необходимости
    """

    def __init__(self, page: Page, locator:str, name:str):
        self.page = page
        self.locator = locator
        self.name =name

    @property
    def type_of(self) -> str:
        return "base element"

    # билдер локатров
    # позволяет динамически сформировать локаторы
    def get_locator(self, nth:int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f"Getting locator with data-test-id={locator} with index {nth}"):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth:int = 0, **kwargs):
        with allure.step(f"Clicking {self.type_of} '{self.name}'"):
            locator = self.get_locator(**kwargs).nth(nth)
            locator.click()

    def check_visible(self, nth:int = 0, **kwargs):
        with allure.step(f"Checking visibility of"
                         f" {self.type_of} '{self.name}'"):
            locator = self.get_locator(**kwargs).nth(nth)
            expect(locator).to_be_visible()

    def check_text(self, expected_text:str, nth:int = 0,**kwargs):
        with allure.step(f"Checking {self.type_of} '{self.name}' text"):
            locator = self.get_locator(**kwargs).nth(nth)
            expect(locator).to_have_text(expected=expected_text)
import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Инпут для загрузки файла
    """
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file:str, nth:int = 0, **kwargs):
        with allure.step(f"Set file {file} to the {self.type_of} '{self.name}' "):
            locator=self.get_locator(nth=nth, **kwargs)
            print("LOCATOR, ", locator)
            locator.set_input_files(files=file)
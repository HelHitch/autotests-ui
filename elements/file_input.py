from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Инпут для загрузки файла
    """

    def set_input_files(self, file:str, nth:int = 0, **kwargs):
            locator=self.get_locator(nth=nth, **kwargs)
            locator.set_input_files(files=file)
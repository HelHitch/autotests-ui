from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier = identifier
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page=page,
                                   locator="{identifier}-image-upload-widget-preview-image",
                                   name="Preview image")

        self.image_upload_info_icon = Icon(page=page,
                                           locator="{identifier}-image-upload-widget-info-icon",
                                           name="Image Upload Icon")
        self.image_upload_info_title = Text(page=page,
                                            locator="{identifier}-image-upload-widget-info-title-text",
                                            name="Image Upload Title")
        self.image_upload_info_description = Text(page=page,
                                                  locator="{identifier}-image-upload-widget-info-description-text",
                                                  name="Image Upload Description")

        self.upload_button = Button(page=page,
                                    locator="{identifier}-image-upload-widget-upload-button",
                                    name="Upload Image Button")
        self.remove_button = Button(page=page,
                                    locator="{identifier}-image-upload-widget-remove-button",
                                    name="Remove Image Button")
        self.upload_input = FileInput(page=page,
                                      locator="{identifier}-image-upload-widget-input",
                                      name="Upload Image Input")

    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible(identifier=self.identifier)

        self.image_upload_info_title.check_visible(identifier=self.identifier)
        self.image_upload_info_title.check_text(expected_text='Tap on "Upload image" button to select file',
                                                identifier=self.identifier)

        self.image_upload_info_description.check_visible(identifier=self.identifier)
        self.image_upload_info_description.check_text(expected_text='Recommended file size 540X300',
                                                      identifier=self.identifier)

        self.upload_button.check_visible(identifier=self.identifier)


        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible(identifier=self.identifier)
            self.preview_image.check_visible(identifier=self.identifier)

        if not is_image_uploaded:
            # Если картинка yt загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click(identifier=self.identifier)

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file, identifier=self.identifier)
import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.input import Input
from elements.dropdown import DropDown
from elements.checkbox import Checkbox
from elements.window import Window

from tools import fakers


class OrgStructureArchiveFormComponent(BaseComponent):
    """
    Компонент модалки архивации

    """
    ARCHIVE_MODAL_ID = '#archive-structure-item-side-panel-modal'
    def __init__(self, page: Page):
        super().__init__(page)
        self.modal_window=Window(page,self.ARCHIVE_MODAL_ID,'Модалка архивации')
        self.confirm_button = Button(page, f'{self.ARCHIVE_MODAL_ID} [data-test="confirm"]', 'Подтверждение архивации')
        self.cancel_button = Button(page, f'{self.ARCHIVE_MODAL_ID} [data-test="close"]', 'Отмена архивации')

    @allure.step("Check archived modal opened")
    def check_visible_archived_modal_opened(self):

        self.modal_window.check_opened()
        self.confirm_button.check_visible()
        self.cancel_button.check_visible()

    @allure.step("Click confirm button")
    def click_confirm_button(self):
        self.confirm_button.click()
        self.modal_window.check_closed()

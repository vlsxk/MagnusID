import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class OrgStructureTittleComponent(BaseComponent):
    """
Компонент заголовка, содержит
- заголовок
- Плюсик
"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, '.page-header__title', 'Заголовок Структура компании')
        self.tittle_button=Button(page, 'v-page-header-button-add-icon', 'Плюсик создания')

    @allure.step("Check that Org Sctructure title is visible")
    def check_visible(self):
        """
        Проверяет что отображается заголовок и плюсик
        :return:
        """
        self.title.check_visible()
        self.title.check_have_text('Структура компании')

        self.tittle_button.check_visible()
        self.tittle_button.check_enabled()

    @allure.step("Click [+] from title")
    def click_create_plus_from_tittle(self):
        """
        Клик на плюсик в заголовке
        :return:
        """
        self.tittle_button.click()


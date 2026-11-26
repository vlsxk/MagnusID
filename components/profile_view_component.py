import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class ProfileViewComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, '.profile__header.text-h3', 'Профиль')

    @allure.step("Check visible profile toolbar view")
    def check_visible(self):
        # Проверка, что заголовок виден на экране
        self.title.check_visible()
        # Проверка, что заголовок содержит правильный текст
        self.title.check_have_text('Профиль')
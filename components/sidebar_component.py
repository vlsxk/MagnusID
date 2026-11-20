import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text

class SidebarComponent(BaseComponent):
    """
    Компонент бокового меню, где отображаются:
    - MagnusID
    - иконка профиля
    - меню
    - подпись снизу
    """

    def __init__(self, page: Page):
        super().__init__(page)
        """
        тут надо локаторы сайдбара
        """
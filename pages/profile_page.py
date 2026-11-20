
from playwright.sync_api import Page


from components.profile_view_component import ProfileViewComponent

from pages.base_page import BasePage

class ProfilePage(BasePage):

    # def __init__(self, page: Page) -> None:
    #     super().__init__(page)
    #     self.URL=AppRoute.PROFILE
    #     self.profile_title=page.locator('.profile__header.text-h3', has_text='Профиль')
    #
    # def check_opened(self) -> None:
    #     self.check_current_url(self.URL)
    #
    # def check_visible_profile_title(self) -> None:
    #     expect(self.profile_title).to_be_visible()
    #     expect(self.profile_title).to_have_text("Профиль")

    """
    Страница панели управления (Dashboard Page).

    Включает компоненты:
    - Панель навигации (Navbar)
    - Графики по оценкам, курсам, студентам и активностям
    - Панель инструментов для управления

    Наследуется от BasePage.
    """

    def __init__(self, page: Page):
        """
        Инициализация страницы панели управления.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)
        self.profile_toolbar_view = ProfileViewComponent(page)  # Панель инструментов

    def check_visible_profile_tittle(self):
        """
        Проверка видимости графика по студентам.

        :raises AssertionError: Если график не виден или не имеет правильного текста
        """
        self.profile_toolbar_view.check_visible()


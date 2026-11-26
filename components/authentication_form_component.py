import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class AuthenticationFormComponent(BaseComponent):
    """
    Компонент формы аутентификации (логина). Содержит поля: Username, Password.
    Предоставляет методы для заполнения и проверки отображения формы.
    """

    def __init__(self, page: Page):
        """
        Инициализирует компонент формы логина.

        :param page: Экземпляр Playwright Page.
        """

        super().__init__(page)


        self.username_input = Input(page, "login-input-username", "Username")
        # Поле ввода password
        self.password_input = Input(page, "login-input-password", "Password")

    @allure.step("Fill login form")
    def fill(self, username: str, password: str):
        """
        Заполняет форму логина заданными значениями.

        :param username: Имя пользователя.
        :param password: Пароль.
        """

        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step("Check that login form is visible")
    def check_visible(self) -> None:
        """
        Проверяет, что форма логина отображается.
        Если переданы username/password — дополнительно проверяет значения в полях.
.
        """
        self.username_input.check_visible()
        self.password_input.check_visible()


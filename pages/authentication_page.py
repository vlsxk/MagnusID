import time
import re
from playwright.sync_api import Page, expect
from tools.routes import AppRoute
from config import Settings
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from components.authentication_form_component import AuthenticationFormComponent
from pages.profile_page import ProfilePage

class AuthenticationPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.authentication_form = AuthenticationFormComponent(page)
        self.login_link = Link(page, "registration-page-login-link", "Login")  # Ссылка на страницу входа
        self.authentication_button = Button(page, "login-button-sign-in",
                                          "Authentication button")  # Кнопка отправки формы

    def click_authentication_button(self):
        """
        Клик на кнопку "Зарегистрироваться" и проверка перехода на страницу панели управления.

        :raises AssertionError: Если URL не соответствует ожидаемому
        """
        # Нажатие на кнопку регистрации
        self.authentication_button.click()
        # Проверка, что мы перенаправлены на страницу панели управления
        self.check_current_url(re.compile(".*/profile"))









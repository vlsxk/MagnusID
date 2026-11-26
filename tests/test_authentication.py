from time import sleep
import time

from config import Settings
from pages.authentication_page import AuthenticationPage
from pages.profile_page import ProfilePage
import allure
import pytest
from tools.routes import AppRoute

class TestAuthentication:
    @allure.title("Successful authentication")
    def test_successful_authentication(self,
                                       authentication_page: AuthenticationPage,
                                       profile_page: ProfilePage,
                                       settings: Settings
    ):

        authentication_page.visit(AppRoute.AUTH)

        authentication_page.authentication_form.check_visible()
        authentication_page.authentication_form.fill(
            username=settings.admin_username,
            password=settings.admin_password
        )
        # 4. Клик по кнопке регистрации
        authentication_page.click_authentication_button()

        profile_page.check_visible_profile_tittle()


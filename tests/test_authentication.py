from time import sleep
import time

from config import Settings
from pages.authentication_page import AuthenticationPage
from pages.profile_page import ProfilePage
import allure
import pytest
from tools.routes import AppRoute

# def test_successful_authentication(user_data: dict[str, str],
#                                    authentication_page: AuthenticationPage,
#                                    profile_page: ProfilePage
#                                    ) -> None:
#     authentication_page.open_page()
#     authentication_page.check_visible_registration_form()
#     authentication_page.fill_registration_form(
#         username=user_data["username"],
#         password=user_data["password"]
#     )
#     authentication_page.click_registration_button()
#     profile_page.check_opened()
#     profile_page.check_visible_profile_title()
#
#     input("Press enter to continue...")

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


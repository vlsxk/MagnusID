import pytest
from pages.authentication.authentication_page import AuthenticationPage
from pages.profile.profile_page import ProfilePage

def test_successful_authentication(user_data: dict[str, str],
                                   authentication_page: AuthenticationPage,
                                   profile_page: ProfilePage
                                   ) -> None:
    authentication_page.open_page()
    authentication_page.check_visible_registration_form()
    authentication_page.fill_registration_form(
        username=user_data["username"],
        password=user_data["password"]
    )
    authentication_page.click_registration_button()
    profile_page.check_opened()
    profile_page.check_visible_profile_title()

    input("Press enter to continue...")


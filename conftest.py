import pytest
from playwright.sync_api import Page

from pages.authentication.authentication_page import AuthenticationPage
from pages.profile.profile_page import ProfilePage

@pytest.fixture
def user_data() -> dict[str, str]:
    return {
        "username": "testuser",
        "password": "password"
    }

@pytest.fixture
def authentication_page(page: Page) -> AuthenticationPage:
    return AuthenticationPage(page)

@pytest.fixture
def profile_page(page: Page) -> ProfilePage:
    return ProfilePage(page)

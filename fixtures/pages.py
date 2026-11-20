from playwright.sync_api import Playwright, Page, expect
from pages.authentication_page import AuthenticationPage
from pages.profile_page import ProfilePage
from pages.org_structure_page import OrgStructurePage
import pytest



@pytest.fixture
def authentication_page(unauthorized_page: Page) -> AuthenticationPage:
    return AuthenticationPage(page=unauthorized_page)


@pytest.fixture
def profile_page(unauthorized_page: Page) -> ProfilePage:
    return ProfilePage(page=unauthorized_page)


@pytest.fixture(scope="module")
def org_structure_page(authorized_admin_page: Page) -> OrgStructurePage:
    return OrgStructurePage(page=authorized_admin_page)

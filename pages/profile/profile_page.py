from playwright.sync_api import Page, expect

from pages.base_page import BasePage
class ProfilePage(BasePage):
    URL="https://magnusid-app-dev-k8s.mgns-tech.ru/profile"
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.profile_title=page.locator('.profile__header.text-h3', has_text='Профиль')

    def check_opened(self) -> None:
        self.check_current_url(self.URL)

    def check_visible_profile_title(self) -> None:
        expect(self.profile_title).to_be_visible()
        expect(self.profile_title).to_have_text("Профиль")
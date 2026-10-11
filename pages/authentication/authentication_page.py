from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class AuthenticationPage(BasePage):
    URL="https://magnusid-app-dev-k8s.mgns-tech.ru"
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.locator("#input_1")
        self.password_input = page.locator("#input_2")
        self.registration_button =page.locator('button', has_text='Войти')

    def open_authorization_page(self) -> None:
        super().open(self.URL)

    def check_visible_registration_form(self) -> None:
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.registration_button).to_be_visible()

    def fill_registration_form(self, username:str, password:str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
    def click_registration_button(self):
        self.registration_button.click()




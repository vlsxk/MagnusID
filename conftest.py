import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True для CI
        page = browser.new_page()
        yield page          # тест выполняется здесь
        browser.close()     # гарантированно закрывается после теста
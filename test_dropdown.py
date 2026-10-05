import pytest


@pytest.mark.skip(reason="Причина")
def test_dropdown(page):
    page.goto("https://the-internet.herokuapp.com/dropdown",timeout=60000, wait_until="domcontentloaded")
    dropdown = page.locator('//*[@id="dropdown"]')
    dropdown.select_option(label="Option 2")
    selected_value = dropdown.evaluate("el => el.value")
    assert selected_value == "2", f"Ожидается значение '2', но выбрано '{selected_value}'"


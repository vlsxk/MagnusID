import pytest


@pytest.mark.checkboxes
def test_checkboxes(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes",timeout=60000, wait_until="domcontentloaded")
    checkbox1 = page.locator('//*[@id="checkboxes"]/input[1]')
    checkbox2 = page.locator('//*[@id="checkboxes"]/input[2]')
    checkbox1.check()
    checkbox2.uncheck()
    assert checkbox1.is_checked(), "Первый чекбокс не отмечен"
    assert checkbox2.is_checked(), "Второй чекбокс не отмечен"
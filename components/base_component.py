from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    """
    Базовый компонент страницы.
    Содержит общие методы и интерфейс для всех дочерних компонентов.
    """
    def __init__(self, page: Page):
        self.page = page


    def check_current_url(self, expected_url: Pattern[str]):
        """
        Проверяет, соответствует ли текущий URL страницы заданному шаблону.

        :param expected_url: Шаблон (регулярное выражение), которому должен соответствовать URL.
        """
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'

        # Добавляем шаг в Allure отчёт
        with allure.step(step):
            # Записываем шаг в лог
            logger.info(step)
            # Проверяем, что URL соответствует заданному шаблону
            expect(self.page).to_have_url(expected_url)

    def check_name_visible_on_page(self, text: str, nth: int = 0) -> None:
        """
        Проверяет, что на странице есть видимый элемент с текстом `text`.

        :param text: Текст для поиска (по умолчанию — точное совпадение).
        :param nth: Индекс элемента среди совпадений (0 — первое).
        """
        step = f'Checking that text "{text}" is visible on the page'

        with allure.step(step):
            locator = self.page.get_by_text(text, exact=True).nth(nth)
            logger.info(step)
            expect(locator).to_be_visible()



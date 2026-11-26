import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement:

    def __init__(self, page: Page, locator: str, name: str) -> None:

        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:

        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:

        is_selector = self.locator.startswith((".", "#", "//", "["))

        if is_selector:
            locator = self.locator  # CSS не форматируем — в классах вёрстки бывают фигурные скобки
            description = f'selector "{locator}"'
        else:
            locator = self.locator.format(**kwargs)
            description = f'"data-test={locator}"'

        step = f'Getting locator with {description} at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            if is_selector:
                return self.page.locator(locator).nth(nth)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        """
        Выполняет клик по элементу.

        :param nth: Индекс элемента (по умолчанию 0)
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Проверяет, что элемент видим на странице.

        :param nth: Индекс элемента
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" is visible'


        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Проверяет, что у элемента присутствует заданный текст.

        :param text: Ожидаемый текст
        :param nth: Индекс элемента
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
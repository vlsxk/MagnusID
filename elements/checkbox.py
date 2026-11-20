import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("CHECKBOX")


class Checkbox(BaseElement):
    """
    Класс для работы с чекбоксами на странице. Наследует базовые методы от BaseElement
    и добавляет специфичные методы для работы с флагами: установка, снятие и проверка состояния.
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента, в данном случае "checkbox".
        """
        return "checkbox"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Получает локатор для поля ввода с возможностью параметризации и выбором индекса.
        """
        # Вызываем родительский метод для получения базового локатора и добавляем локатор для input
        # Может быть необходимо если на странице нужно как-то хитро получать поле ввода
        return super().get_locator(nth, **kwargs)

    def is_checked(self, nth: int = 0, **kwargs) -> bool:
        """
        Возвращает текущее состояние чекбокса.

        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :return: True, если чекбокс отмечен, иначе False.
        """
        return self.get_locator(nth, **kwargs).is_checked()

    def check(self, nth: int = 0, **kwargs):
        """
        Отмечает чекбокс. Если он уже отмечен — ничего не делает.

        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        """
        step = f'Checking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            if not locator.is_checked():
                locator.click()

    def uncheck(self, nth: int = 0, **kwargs):
        """
        Снимает отметку с чекбокса. Если он уже снят — ничего не делает.

        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        """
        step = f'Unchecking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            if locator.is_checked():
                locator.click()

    def set_checked(self, state: bool, nth: int = 0, **kwargs):
        """
        Приводит чекбокс к заданному состоянию.

        :param state: True — отметить, False — снять.
        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        """
        if state:
            self.check(nth, **kwargs)
        else:
            self.uncheck(nth, **kwargs)

    def check_is_checked(self, nth: int = 0, **kwargs):
        """
        Проверяет, что чекбокс отмечен.

        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если чекбокс не отмечен.
        """
        step = f'Checking that {self.type_of} "{self.name}" is checked'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_checked()

    def check_is_unchecked(self, nth: int = 0, **kwargs):
        """
        Проверяет, что чекбокс не отмечен.

        :param nth: Индекс, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если чекбокс отмечен.
        """
        step = f'Checking that {self.type_of} "{self.name}" is unchecked'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).not_to_be_checked()

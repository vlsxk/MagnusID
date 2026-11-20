import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("DROPDOWN")

class DropDown(BaseElement):

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента, в данном случае "dropdown".
        Это полезно для унификации работы с различными типами элементов.
        """
        return "dropdown"
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Получает локатор для поля ввода с возможностью параметризации и выбором индекса.
        """
        # Вызываем родительский метод для получения базового локатора и добавляем локатор для input
        # Может быть необходимо если на странице нужно как-то хитро получать поле ввода
        return super().get_locator(nth, **kwargs)

    def get_option_locator(self, option_text: str) -> Locator:
        """
        Получает локатор опции в открывшемся списке.

        Сначала пробуем семантичный поиск по роли option,
        при отсутствии ролей в вёрстке — фильтр по тексту среди элементов меню.
        Переопределите, если структура списка на вашем проекте отличается.

        :param option_text: Текст опции, которую нужно выбрать.
        :return: Локатор опции.
        """
        by_role = self.page.get_by_role("option", name=option_text)
        if by_role.count() > 0:
            return by_role
        return self.page.locator(
            f'.dropdown-item, [role="option"]'
        ).filter(has_text=option_text)

    def select_locator_text(self, value: str, nth: int = 0, **kwargs):
        """
        Открывает выпадающий список и выбирает опцию по тексту.

        :param value: Текст опции, которую нужно выбрать.
        :param nth: Индекс, если на странице несколько одинаковых списков.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если список или опция не найдены.
        """
        step = f'Select {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            input_locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            input_locator.click()

            option = self.get_option_locator(value)
            option.wait_for(state="visible")
            option.click()

    def select(self, value: str, nth: int = 0, **kwargs):
        """
        Открывает выпадающий список и выбирает опцию по тексту.

        :param value: Текст опции, которую нужно выбрать.
        :param nth: Индекс, если на странице несколько одинаковых списков.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если список или опция не найдены.
        """
        step = f'Select {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            logger.info(step)
            input_locator = self.get_locator(nth, **kwargs)
            # input_locator.click()

            # Опцию ищем внутри локатора компонента (он уже содержит
            # реальный селектор пункта меню), а не по generic-шаблону
            option = self.get_locator(nth, **kwargs).filter(has_text=value).first
            option.wait_for(state="visible")
            option.click()

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Проверяет, что в поле списка отображается выбранное значение.

        :param value: Ожидаемое значение в поле.
        :param nth: Индекс, если на странице несколько одинаковых списков.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если значение в поле не соответствует ожидаемому.
        """
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

    def check_is_open(self, nth: int = 0, **kwargs):
        """
        Проверяет, что список открыт: хотя бы одна опция видна.
        """
        step = f'Checking that {self.type_of} "{self.name}" is open'

        with allure.step(step):
            logger.info(step)
            expect(self.page.locator('[role="option"], .dropdown-item').first).to_be_visible()

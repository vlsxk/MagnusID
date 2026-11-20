import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("WINDOW")


class Window(BaseElement):
    """
    Класс для работы с модальными окнами (диалогами). Наследует базовые методы
    от BaseElement и добавляет специфичные методы: проверка открытости/закрытости,
    закрытие через крестик и получение заголовка.

    В качестве локатора обычно передаётся контейнер модалки,
    например data-test="create-department-modal".
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента, в данном случае "window".
        """
        return "window"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Получает локатор для поля ввода с возможностью параметризации и выбором индекса.
        """
        # Вызываем родительский метод для получения базового локатора и добавляем локатор для input
        # Может быть необходимо если на странице нужно как-то хитро получать поле ввода
        return super().get_locator(nth, **kwargs)

    def check_opened(self, nth: int = 0, **kwargs):
        """
        Проверяет, что модальное окно открыто и видно на странице.

        :param nth: Индекс, если на странице несколько одинаковых окон.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если окно не открыто.
        """
        step = f'Checking that {self.type_of} "{self.name}" is opened'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_closed(self, nth: int = 0, **kwargs):
        """
        Проверяет, что модальное окно закрыто.

        :param nth: Индекс, если на странице несколько одинаковых окон.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если окно всё ещё открыто.
        """
        step = f'Checking that {self.type_of} "{self.name}" is closed'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).not_to_be_visible()

    def close(self, nth: int = 0, close_button_locator: str | None = None, **kwargs):
        """
        Закрывает модальное окно.

        По умолчанию ищет кнопку закрытия внутри окна по роли button
        и доступному имени. Если в вёрстке крестик не имеет имени,
        передайте селектор кнопки через close_button_locator.

        :param nth: Индекс, если на странице несколько одинаковых окон.
        :param close_button_locator: Селектор кнопки закрытия (опционально).
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        """
        step = f'Closing {self.type_of} "{self.name}"'

        with allure.step(step):
            window_locator = self.get_locator(nth, **kwargs)
            logger.info(step)

            if close_button_locator:
                close_button = window_locator.locator(close_button_locator)
            else:
                close_button = window_locator.get_by_role("button", name="Close")

            close_button.click()

    def get_title(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает локатор заголовка окна.

        По умолчанию ищет первый заголовок (h1–h4) внутри контейнера окна.
        Переопределите или передайте свой селектор, если заголовок устроен иначе.

        :param nth: Индекс, если на странице несколько одинаковых окон.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :return: Локатор заголовка.
        """
        return self.get_locator(nth, **kwargs).locator("h1, h2, h3, h4").first

    def check_have_title(self, title: str, nth: int = 0, **kwargs):
        """
        Проверяет, что заголовок модального окна содержит заданный текст.

        :param title: Ожидаемый текст заголовка.
        :param nth: Индекс, если на странице несколько одинаковых окон.
        :param kwargs: Дополнительные аргументы для параметризации локатора.
        :raises AssertionError: Если текст заголовка не совпадает.
        """
        step = f'Checking that {self.type_of} "{self.name}" has title "{title}"'

        with allure.step(step):
            locator = self.get_title(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(title)

import pytest

from pages.org_structure_page import OrgStructurePage
from tools.routes import AppRoute


@pytest.fixture(scope="module")
def created_organization_name(org_structure_page: OrgStructurePage) -> dict:
    # 1. Переход на страницу Структуры компании
    org_structure_page.visit(AppRoute.ORG_STRUCTURE)

    # 2. Проверка отображения заголовка
    org_structure_page.title_component.check_visible()

    # 3. Нажимаем на плюсик
    org_structure_page.title_component.click_create_plus_from_tittle()

    # 4. Проверяем что открылась модалка с выбором
    org_structure_page.create_choice_modal.check_visible()

    # 5. Нажимаем в модалке на Организация
    org_structure_page.create_choice_modal.click_button_create_organization()

    # 6. Проверяем что модалка создания Организации открылась и содержит все необходимые компоненты
    org_structure_page.create_organization_form.check_visible_organization_create_form_from_tittle()

    # 7. Заполняем модалку создания организации
    name=org_structure_page.create_organization_form.fill_organization_create_form_from_tittle()

    # 7. Нажимаем сохранить
    org_structure_page.create_organization_form.click_save_button()

    # 8 Проверяем что видим.
    org_structure_page.tree_component.check_name_visible_on_page(name)
    holder = {"name": name}

    yield holder

    current_name = holder["name"]  # актуальное имя (edit-тест мог его обновить)

    org_structure_page.tree_component.click_tree_element(current_name)

    org_structure_page.modal_component.click_options_and_archive()
    org_structure_page.archive_modal.check_visible_archived_modal_opened()
    org_structure_page.archive_modal.click_confirm_button()


    org_structure_page.reload()
    org_structure_page.tree_component.check_name_not_visible(current_name)








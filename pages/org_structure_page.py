from playwright.sync_api import Page, expect
import tools.fakers as fakers
from components.orgstructure_create_form_component import OrgStructureCreateFormComponent
from components.orgstructure_create_form_component import OrgStructureChoiceFormForCreateComponent
from components.orgstructure_modal_component import OrgStructureModalComponent
from components.orgstructure_tittle_component import OrgStructureTittleComponent
from components.orgstructure_tree_component import OrgStructureTreeComponent
from components.orgstructure_archive_form_component import OrgStructureArchiveFormComponent
from pages.base_page import BasePage
import allure
from tools.routes import AppRoute
from elements.text import Text
from elements.button import Button

class OrgStructurePage(BasePage):
    """
    Страница Структуры компании

    Включает компоненты:
    - Меню справа
    - Заголовок с +
    - Модалка создания
    - Дерево
    - Карточка

    """
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        #Компоненты и действия при создании
        self.create_organization_form=OrgStructureCreateFormComponent(page)
        #компоненты модалки выбора
        self.create_choice_modal=OrgStructureChoiceFormForCreateComponent(page)
        #компоненты заголовка
        self.title_component=OrgStructureTittleComponent(page)

        self.tree_component=OrgStructureTreeComponent(page)

        self.modal_component=OrgStructureModalComponent(page)

        self.archive_modal=OrgStructureArchiveFormComponent(page)
        self.entity_type_organization="Organization"

    def open_organization_modal(self, created_organization_name: dict):
        self.tree_component.check_name_visible_on_page(created_organization_name["name"])
        self.tree_component.click_tree_element(created_organization_name["name"])

    def edit_organization_modal(self, org_name: str, org_code: str, org_description: str):
        self.modal_component.click_edit_button()
        edited_organization_name = self.modal_component.fill_organization_modal(org_name, org_code, org_description)
        self.modal_component.click_save_button()
        return edited_organization_name
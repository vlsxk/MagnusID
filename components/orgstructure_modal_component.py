import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.input import Input
from elements.dropdown import DropDown
from elements.checkbox import Checkbox
from elements.window import Window

from tools import fakers


class OrgStructureModalComponent(BaseComponent):
    """
    Компонент карточки

    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.window=Window(page,'side-panel__base','Карточка открыта')
        self.edit_button=Button(page,'v-side-panel-button-edit','Кнопка редактировать')
        self.option_button=Button(page,'options','Кебаб')
        self.archive_dropdown_button=DropDown(page,'.v-dropdown-item:has-text("Архивировать"):visible','Кнопка архивировать')
        self.name_input=Input(page,'company-structure-side-panel-input-name','Инпут имени')
        self.code_input=Input(page,'company-structure-side-panel-input-code','Инпут кода')
        self.description_input=Input(page,'company-structure-side-panel-textarea-description','Инпут описания')
        self.save_button=Button(page,'v-side-panel-button-save-changes','Кнопка Сохранить')
        self.cancel_button=Button(page,'v-side-panel-button-cancel','Кнопка Отменить')


    @allure.step("Click edit button")
    def click_edit_button(self):
        self.edit_button.click()

    @allure.step("fill organization form")
    def positive_fill_organization_modal(self):
        edited_organization_name=fakers.get_string_AQA_type_date("Edited organization name")
        self.name_input.fill(edited_organization_name)
        self.code_input.fill(fakers.get_string_AQA_type_date("Edited organization code"))
        self.description_input.fill(fakers.get_string_AQA_type_date("Edited organization description"))
        return edited_organization_name

    @allure.step("fill organization form")
    def fill_organization_modal(self, organization_name:str, organization_code:str, organization_description:str):
        self.name_input.fill(organization_name)
        self.code_input.fill(organization_code)
        self.description_input.fill(organization_description)
        return organization_name

    @allure.step("Click save button")
    def click_save_button(self):
        self.save_button.click()

    @allure.step("Click archive button")
    def click_options_and_archive(self):

        self.option_button.check_visible()
        self.option_button.click()

        self.archive_dropdown_button.select("Архивировать")

    @allure.step("Click {name} in modal")
    def click_visible_element_by_name(self, name: str) -> None:
        modal = self.page.locator('.v-dropdown.profile-dropdown')
        modal.get_by_text(name, exact=True).click()









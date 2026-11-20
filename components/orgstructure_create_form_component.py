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


class OrgStructureCreateFormComponent(BaseComponent):
    """
    Компонент формы создания элементов структуры компании, а точнее
    - Модальное окно

    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.organization_create_form_window=Window(page,'#create-department','Модальное окно создания')
        self.organization_create_form_input_name=Input(page,'create-department-modal-input-name', 'Поле ввода названия' )
        self.organization_create_form_parent_selector=DropDown(page,'.department-tree-select__trigger','Выпадающее поле Родительский элемент')
        self.organization_create_form_input_code=Input(page, 'create-department-modal-input-code', 'Поле ввода кода')
        self.organization_create_form_input_description=Input(page, 'create-department-modal-textarea-description' , 'Поле ввода описания' )
        self.organization_create_form_save_button=Button(page, 'create-department-modal-button-save', 'Кнопка "Сохранить"' )
        self.organization_create_form_cancel_button=Button(page, 'create-department-modal-button-cancel' , 'Кнопка "Отменить"')
        self.organization_create_form_manager_selector=DropDown(page,'create-department-modal-select-manager','Выпадающее поле Начальник')
        self.organization_create_form_checkbox=Checkbox(page,'create-department-modal-checkbox-is-main', 'Чекбокс Сделать основным')


    @allure.step("Check visible organization modal create form from tittle")
    def check_visible_organization_create_form_from_tittle(self):
        """
        Проверка отображения окна создания Организации из [+] в заголовке
        :return:
        """
        self.organization_create_form_window.check_opened()
        self.organization_create_form_input_name.check_visible()
        self.organization_create_form_parent_selector.check_visible()
        self.organization_create_form_input_code.check_visible()
        self.organization_create_form_input_description.check_visible()

    @allure.step("Fill create organization form")
    def fill_organization_create_form_from_tittle(self):
        """
        Заполняем все поля модалки создания организации
        :return:
        """
        created_organization_name=fakers.get_string_AQA_type_date("Organization name")

        self.organization_create_form_input_name.fill(created_organization_name)
        self.organization_create_form_input_code.fill(fakers.get_string_AQA_type_date("Organization code"))
        self.organization_create_form_input_description.fill(fakers.get_string_AQA_type_date("Organization description"))
        return created_organization_name

    @allure.step("Click save button")
    def click_save_button(self):
        self.organization_create_form_save_button.click()





class OrgStructureChoiceFormForCreateComponent(BaseComponent):
    """
    Компонент, связанный с модальными окнами, появляющимися нажатием [+] из заголовка или из дерева
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.choice_form_menu=Window(page,'.add-menu','Модальное окно с выбором Организации или подразделения для создания')
        self.choice_form_organization = Button(page,'.v-dropdown-item:has-text("Добавить организацию")',"Добавить организацию")
        self.choice_form_departament = Button(page, '.v-dropdown-item:has-text("Добавить подразделение")',"Добавить подразделение")

    @allure.step("Check modal form with choice Organization or Departament is opened ")
    def check_visible(self):
        """
        Проверяет что модалка открылась, видна и доступны варианты создания
        :return:
        """
        self.choice_form_menu.check_opened()

        self.choice_form_organization.check_visible()
        self.choice_form_organization.check_enabled()

        self.choice_form_departament.check_visible()
        self.choice_form_departament.check_enabled()

    @allure.step("Click Organization in modal")
    def click_button_create_organization(self):
        """
        В модалке выбираем Организацию
        :return:
        """
        self.choice_form_organization.click()









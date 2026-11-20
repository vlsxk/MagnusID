import pytest
from pages.org_structure_page import OrgStructurePage
import tools.fakers as fakers

import allure

from tools.routes import AppRoute


class TestCreateOrganization:
    entity_type_organization="Organization"
    @pytest.mark.regression
    @allure.title("Successful create and edit organization")
    def test_create_organization(self, org_structure_page: OrgStructurePage,
                                 created_organization_name:dict):

        org_structure_page.tree_component.check_name_visible_on_page(created_organization_name["name"])

    # @pytest.mark.regression
    # def test_edit_organization(self, org_structure_page: OrgStructurePage,
    #                            created_organization_name: str):
    #     org_structure_page.visit(AppRoute.ORG_STRUCTURE)
    #     org_structure_page.tree_component.check_name_visible_on_page(created_organization_name)
    #     org_structure_page.tree_component.click_tree_element(created_organization_name)
    #     org_structure_page.modal_component.click_edit_button()
    #     edited_organization_name = org_structure_page.modal_component.fill_organization_modal()
    #     created_organization_name["name"] = edited_organization_name
    #     org_structure_page.modal_component.click_save_button()
    #     org_structure_page.reload()
    #     org_structure_page.tree_component.check_name_visible_on_page(edited_organization_name)

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "org_name, org_code, org_description",
        [

            (fakers.get_len_string_AQA_type_date(entity_type_organization, length=1),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=1),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=1)),
            (fakers.get_len_string_AQA_type_date(entity_type_organization, length=10),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=10),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=10)),
            (fakers.get_len_string_AQA_type_date(entity_type_organization, length=255),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=100),
             fakers.get_len_string_AQA_type_date(entity_type_organization, length=500))
        ],
        ids=["1", "basic", "max"],
    )
    def test_edit_organization(self, org_structure_page: OrgStructurePage,
                               created_organization_name: dict,
                               org_name: str,
                               org_code: str,
                               org_description: str):
        org_structure_page.visit(AppRoute.ORG_STRUCTURE)

        org_structure_page.tree_component.check_name_visible_on_page(created_organization_name["name"])
        org_structure_page.tree_component.click_tree_element(created_organization_name["name"])

        org_structure_page.modal_component.click_edit_button()
        edited_organization_name = org_structure_page.modal_component.fill_organization_modal(org_name,org_code,org_description)

        org_structure_page.modal_component.click_save_button()
        created_organization_name["name"] = edited_organization_name
        # org_structure_page.reload()
        org_structure_page.visit(AppRoute.ORG_STRUCTURE)

        org_structure_page.tree_component.check_name_visible_on_page(edited_organization_name)











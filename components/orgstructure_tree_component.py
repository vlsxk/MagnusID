import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
class OrgStructureTreeComponent(BaseComponent):
    """
Компонент заголовка, содержит дерево
"""
    def __init__(self, page: Page):
        super().__init__(page)

        self.expand_tree_button=Button(page,'.v-tree__arrow-wrap.v-tree__arrow-wrap--clickable','стрелочка для раскрытия дерева')

    @allure.step("Click {name} in tree")
    def click_tree_element(self,name: str) -> None:
        tree = self.page.locator('.company-tree')
        tree.get_by_text(name, exact = True).click()







    @allure.step("Expand tree node '{name}' if collapsed")
    def expand_tree_node(self, name: str) -> None:
        node = self.tree.get_by_role("treeitem").filter(has_text=name).first

        if node.get_attribute("aria-expanded") == "false":
            node.locator(self.expand_tree_button).click()
            # ждём, пока состояние изменится
            expect(node).to_have_attribute("aria-expanded", "true")

    @allure.step("Check that '{name}' is visible in tree")
    def check_name_visible_on_page(self, name: str, *, parent_name: str | None = None) -> None:
        if not isinstance(name, str):
            raise TypeError(
                f"check_name_visible_on_page ждёт строку с именем организации, "
                f"а получено {type(name).__name__}: {name!r}. "
                f"Вероятно, передан контейнер фикстуры вместо created_organization_name['name']."
            )

        if parent_name:
            self.expand_tree_node(parent_name)  # если дети подгружаются лениво

        tree = self.page.locator('.company-tree')
        expect(tree.get_by_text(name, exact=True)).to_be_visible()



    @allure.step("Check that '{name}' is NOT visible on page")
    def check_name_not_visible(self, name: str) -> None:
        tree = self.page.locator('.company-tree')
        expect(tree.page.get_by_text(name, exact=True)).not_to_be_visible()
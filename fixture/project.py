from selenium.webdriver.support.select import Select
from model.Project_details import ProjectDetails

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("project_NAME")
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text("release")
        wd.find_element_by_xpath("//option[@value='30']").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_xpath("(//option[@value='10'])[2]").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("this is test!!!")
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("tr.row-1 > td > a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("tr.row-1 > td > a"))

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            self.project_cache = []
            for row in wd.find_elements_by_tag_name("tr"):
                cell = row.find_elements_by_xpath("//*[@id='content']/div[2]/table/tbody/tr/td")
                text_projectname = cell[0].text
                text_description = cell[4].text
                self.project_cache.append(ProjectDetails(name=text_projectname, description=text_description))
        return list(self.project_cache)



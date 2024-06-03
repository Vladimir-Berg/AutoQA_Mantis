import time
from model.project import Project

from selenium.webdriver.common.by import By


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_projects(self):
        wd = self.app.driver
        wd.get(self.app.base_url + "/manage_proj_page.php")

    def create_new_project(self, project):
        wd = self.app.driver
        self.open_manage_projects()
        wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        wd.find_element(By.CSS_SELECTOR, "input[name='name']").click()
        wd.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(project.name)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()

    list_of_projects = []

    def delete_project(self, project_id):
        wd = self.app.driver
        self.open_manage_projects()
        for item in (wd.find_element(By.CSS_SELECTOR, 'body > table:nth-child(6) > tbody').
                        find_elements(By.CSS_SELECTOR, "tbody > tr"))[2:]:
            href = item.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a").get_attribute('href')
            if int(href.split('=')[1]) == project_id:
                item.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a").click()
                wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
                wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
                break

    def get_list_projects(self):
        wd = self.app.driver
        self.open_manage_projects()
        self.list_of_projects = []
        for item in (wd.find_element(By.CSS_SELECTOR, 'body > table:nth-child(6) > tbody').
                        find_elements(By.CSS_SELECTOR, "tbody > tr"))[2:]:
            name = item.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
            id = item.find_element(By.CSS_SELECTOR, "td:nth-child(1) > a").get_attribute('href')
            id = id.split('=')[1]
            self.list_of_projects.append(Project(name=name, id=id))
        return self.list_of_projects

from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_of_projects(self, username, password):
        projects = []
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            list_of_projects = client.service.mc_projects_get_user_accessible(username, password)
            for item in list_of_projects:
                name = item.name
                id = item.id
                project = Project(name, id)
                projects.append(project)

            return projects

        except WebFault:
            return False

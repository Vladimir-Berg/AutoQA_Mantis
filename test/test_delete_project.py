import random
import string
from model.project import Project


def random_project(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_delete_project(app):
    project = random_project("project", 10)
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_list = app.soap.get_list_of_projects(username, password)
    if len(old_list) == 0:
        app.project.create_new_project(project)
    old_list = app.soap.get_list_of_projects(username, password)
    project = random.choice(old_list)
    app.project.delete_project(project.id)
    new_list = app.soap.get_list_of_projects(username, password)
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

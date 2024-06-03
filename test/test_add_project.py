from model.project import Project
import string
import random


def random_project(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = random_project("project", 10)
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_list = app.soap.get_list_of_projects(username, password)
    project = Project(project)
    app.project.create_new_project(project)
    new_list = app.soap.get_list_of_projects(username, password)
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
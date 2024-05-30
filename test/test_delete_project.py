import random

from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_list_projects()
    if len(old_list) == 0:
        project = Project('111')
        app.project.create_new_project(project)
    old_list = app.project.get_list_projects()
    project = random.choice(old_list)
    app.project.delete_project(project.id)
    new_list = app.project.get_list_projects()
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

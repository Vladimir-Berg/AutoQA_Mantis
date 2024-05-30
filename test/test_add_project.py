from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_list_projects()
    project = Project('3')
    app.project.create_new_project(project)
    new_list = app.project.get_list_projects()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
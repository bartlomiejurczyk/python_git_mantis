
def delete_project(app):
    app.session.login("administrator", "root")
    if app.project.count() == 0:
        app.project.add_project()
    old_list = app.project.get_project_list()
    app.project.delete_project()
    new_list = app.project.get_project_list()
    assert len(new_list) == len(old_list) + 1
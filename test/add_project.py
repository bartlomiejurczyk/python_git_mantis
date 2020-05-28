
def add_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_project_list()
    app.project.add_project()
    new_list = app.project.get_project_list()
    assert len(new_list) == len(old_list) + 1
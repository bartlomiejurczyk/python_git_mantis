
def delete_project(app):
    app.session.login("administrator", "root")
    if app.project.count() == 0:
        app.project.add_project()
    app.project.delete_project()
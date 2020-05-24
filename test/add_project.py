
def add_project(app):
    app.session.login("administrator", "root")
    app.project.add_project()
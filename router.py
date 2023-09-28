from views import CustomView, custom_view


class Router:
    def __init__(self, app):
        self.app = app
        self.app.register_blueprint(custom_view)
        self.app.add_url_rule('/custom-view/', view_func=CustomView.as_view('custom-view'))

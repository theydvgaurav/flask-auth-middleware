from flask import jsonify, make_response
from flask.views import MethodView


class BaseView(MethodView):
    @staticmethod
    def get_response(data, status_code=200):
        return make_response(jsonify(data), status_code)

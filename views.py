from flask import Blueprint

from base.auth_middleware import require_authentication
from base.views import BaseView

custom_view = Blueprint('custom-view', __name__)


class CustomView(BaseView):
    @require_authentication
    def get(self):
        return self.get_response(data={"message": "Hello There!"})

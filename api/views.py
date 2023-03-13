from flask import Blueprint
from flask_restful import Api

from api.resources.user import UserList, UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(UserList, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")

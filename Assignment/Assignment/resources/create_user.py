import logging
from flask_restful import Resource, request
from operations.Users import user_creation
from shared.responses import raise_exception, get_response
logger = logging.getLogger()
import json


class CreateUser(Resource):
    """
    Its a sign up so no authorization required
    To create the user.
    """

    def post(self):
        try:
            json_data = request.get_json()
            user_created = user_creation.create_user(json_data['data'])
            return get_response(data=user_created, code=201)
        except Exception as e:
            logger.error(e)
            return {"error": str(e)}

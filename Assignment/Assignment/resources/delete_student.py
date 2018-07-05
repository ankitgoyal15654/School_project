import logging
from flask_restful import Resource, request
from operations.Users import sudent_deletion
from shared.responses import get_response
from flask_jwt_extended import jwt_required
logger = logging.getLogger()


class DeleteStudent(Resource):
    """
    To delete the student only admin
    can perform this operation
    """
    @jwt_required
    def delete(self):
        try:
            json_data = request.get_json()
            response = sudent_deletion.deletion_of_student(json_data[
                'data'])
            return get_response(data=response, code=201)
        except Exception as e:
            logger.error(e)
            return {"error": str(e)}

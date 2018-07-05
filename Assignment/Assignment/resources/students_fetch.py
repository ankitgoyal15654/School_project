import logging
from flask_restful import Resource, request
from operations.Users import fetch_student
from shared.responses import  get_response
logger = logging.getLogger()
from flask_jwt_extended import jwt_required


class StudentsFetch(Resource):
    """
    To fetch all the students details
    only by admin
    """

    @jwt_required
    def get(self, username):
        try:
            student_details = fetch_student.find_all_student(username)
            return get_response(data=student_details, code=201)
        except Exception as e:
            logger.error(e)
            return {"error": str(e)}

from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required
from operations.Courses import create_course
from shared.responses import get_response


class CreationOfCourse(Resource):
    """
    To create the course only admin
    can create the courses
    """

    @jwt_required
    def post(self):
        try:
            data = request.get_json()
            response = create_course.creation_of_courses(data["data"])
            return get_response(data=response)
        except Exception as e:
            return {"error": str(e)}

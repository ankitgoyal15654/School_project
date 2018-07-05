from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required
from operations.student_course_mapping import map_courses
from shared.responses import get_response


class CourseMapp(Resource):
    """
    To enroll the courses for the student
    """

    @jwt_required
    def post(self):
        try:
            data = request.get_json()
            response = map_courses.maping_of_courses(data["data"])
            return get_response(data=response)
        except Exception as e:
            return {"error": str(e)}

from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required
from operations.student_course_mapping import unassign_courses
from shared.responses import get_response


class UnassignCourse(Resource):
    """
    To unmap the student from course
    """

    @jwt_required
    def put(self):
        try:
            data = request.get_json()
            response = unassign_courses.unassigned_courses(data["data"])
            return get_response(data=response)
        except Exception as e:
            return {"error": str(e)}

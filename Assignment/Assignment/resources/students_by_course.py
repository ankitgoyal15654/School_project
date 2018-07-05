from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from operations.student_course_mapping import students_by_course
from shared.responses import get_response
from flask_jwt_extended import jwt_required


class StudentByCourse(Resource):
    """
    to fetch students according to the
    that is enrolling courses
    """

    @jwt_required
    def get(self, course_id):
        try:
            course_details = students_by_course.fetch_students_by_courses(
                course_id)
            response = get_response(data=course_details)
            return response, 200
        except Exception as e:
            return {"error": str(e)}, 404

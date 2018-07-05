from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from operations.Courses import courses_fetch
from shared.responses import get_response
from flask_jwt_extended import jwt_required


class FetchCourses(Resource):
    """
    To fetch all the course that is not
    enrolled
    """
    @jwt_required
    def get(self):
        try:
            course_details = courses_fetch.fetch_courses()
            response = get_response(data=course_details)
            return response, 200
        except Exception as e:
            return {"error": str(e)}, 404

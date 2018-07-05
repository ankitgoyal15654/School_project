from models.courses import Courses
import logging
from db import db
logger = logging.getLogger()


def fetch_courses():
    """
    To fetch all the courses
    """
    course_details = db.session.query(Courses).all()
    db.session.commit()
    response = []
    for course in course_details:
        result = {}
        result["id"] = course.id
        result["name"] = course.name
        result["student_enrolled"] = course.student_enrolled
        response.append(result)
    return response

from models.student_Course_mapping import StudentCourseMapping
from models.users import Users
import logging
from db import db
logger = logging.getLogger()


def fetch_students_by_courses(course_id):
    details = db.session.query(
        StudentCourseMapping).filter_by(course_id=course_id).all()
    student_ids = []
    for course in details:
        student_ids.append(course.student_id)
    response = fetch_students(student_ids)
    return response



def fetch_students(student_ids):
    student_details = db.session.query(Users).filter(
        Users.id.in_(student_ids)).all()
    response = []
    for student in student_details:
        result = {}
        result["firstname"] = student.first_name
        result["username"] = student.username
        result["id'"] = student.id
        result["address"] = student.address
        response.append(result)
    return response

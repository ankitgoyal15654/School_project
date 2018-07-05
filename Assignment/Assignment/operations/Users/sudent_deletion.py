from models.users import Users
from models.student_Course_mapping import StudentCourseMapping
from models.courses import Courses
from . import role_details
import logging
from db import db
logger = logging.getLogger()


def deletion_of_student(data):
    '''
  {"data":{   "student_id" : "1",
  "username":"a123"}}
  To delete the student
    '''
    role_detail = role_details.find_user_role(data["username"])
    if role_detail["role_name"].lower() == 'admin':
        remove_site_course_mapping(data["student_id"])
        student_details = Users.query.filter_by(
            id=data["student_id"]).first()
        print student_details

        db.session.delete(student_details)
        db.session.commit()
        return {"id": data["student_id"]}
    else:
        return {"error": "don't have access to delete students"}


def remove_site_course_mapping(student_id):
    """
    To remove the site_course
    mapping
    """
    details = db.session.query(StudentCourseMapping).filter_by(
        student_id=student_id).all()
    if len(details) != 0:
        print "going into if"
        for course in details:
            course_id = course.course_id
            update_course(course_id)
        delete_details = db.session.query(StudentCourseMapping).filter_by(
            student_id=student_id).delete()
        db.session.commit()
    else:
        return


def update_course(course_id):
    """
    when the student is un rolling the course
    student_enrolled is updating
    """
    details = db.session.query(Courses).filter_by(id=course_id).first()
    student_enrolled = details.student_enrolled
    student_enrolled = student_enrolled - 1
    update_course = db.session.query(Courses).filter_by(id=course_id).update(
        {"student_enrolled": int(student_enrolled)})
    db.session.commit()

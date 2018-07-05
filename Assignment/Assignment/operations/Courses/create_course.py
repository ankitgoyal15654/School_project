from models.courses import Courses
from operations.Users import role_details
import logging
from db import db
logger = logging.getLogger()
from datetime import datetime


def creation_of_courses(data):
    """
  {"data":{   "course_name" : "a123",
  "username":"ai23"}}
  To create the courses
    """
    role_detail = role_details.find_user_role(data["username"])
    if role_detail["role_name"].lower() == 'admin':
        course_name = data["course_name"]
        obj = Courses(name=course_name, created_datetime=datetime.now(),
                      is_active=True, student_enrolled=0,
                      modified_datetime=datetime.now())
        db.session.add(obj)
        db.session.commit()
        course_detail = db.session.query(
            Courses).filter_by(name=course_name).first()
        return {"id": course_detail.id}
    else:
        return {"error": "don't have access to create course"}


def deletion_of_courses(data):
    """
  {"data":{   "course_id" : "1",
  "username":"ai23"}}
  To delete the courses
    """
    role_detail = role_details.find_user_role(data["username"])
    if role_detail["role_name"].lower() == 'admin':
        try:
            obj_to_del = Courses.query.filter_by(
                id=data["course_id"]).first()
        except Exception as e:
            return {"error": "can't delete student is enrolling this course"}

        db.session.delete(obj_to_del)
        db.session.commit()
        return {"id": data["course_id"]}
    else:
        return {"error": "don't have access to delete course"}

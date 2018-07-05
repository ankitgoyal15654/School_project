from models.student_Course_mapping import StudentCourseMapping
from models.courses import Courses
import logging
from db import db
from sqlalchemy import and_
logger = logging.getLogger()


def unassigned_courses(data):
    """
  {"data":{   "student_id" : "1",
            "course_id":3
  "username":"a123"}}
  To unassign the courses
    """

    course_details = db.session.query(StudentCourseMapping).filter(and_(StudentCourseMapping.student_id == data[
        "student_id"], StudentCourseMapping.course_id == data["course_id"])).first()
    print course_details
    if course_details is not None:
        update_course(data["course_id"])
        db.session.delete(course_details)
        db.session.commit()
        return {"id": data["course_id"]}
    else:
        return {"message": "no such course mapped"}


def update_course(course_id):
    details = db.session.query(Courses).filter_by(id=course_id).first()
    student_enrolled = details.student_enrolled
    student_enrolled = student_enrolled - 1
    update_course = db.session.query(Courses).filter_by(id=course_id).update(
        {"student_enrolled": int(student_enrolled)})
    db.session.commit()

from models.courses import Courses
from models.student_Course_mapping import StudentCourseMapping
import logging
from db import db
from sqlalchemy import and_
logger = logging.getLogger()


def maping_of_courses(data):
    """
    {
    "data":{"username":"a123",
             "user_id" : "15042",
             "course_id" : 1
    }
    }
    To map the courses to students
    """

    student_id = data["user_id"]
    course_id = data["course_id"]
    details_of_courses = db.session.query(
        Courses).filter_by(id=course_id).first()
    student_enrolled = details_of_courses.student_enrolled
    if student_enrolled < 5:
        obj = StudentCourseMapping(student_id=student_id, course_id=course_id)
        db.session.add(obj)
        db.session.commit()
        details = db.session.query(StudentCourseMapping).filter(and_(
            StudentCourseMapping.student_id == student_id, StudentCourseMapping.course_id == course_id)).first()
        update_course = db.session.query(Courses).filter_by(id=course_id).update(
            {"student_enrolled": (int(student_enrolled) + 1)})
        db.session.commit()

        return {"id": details.id}
    else:
        return {"success": False, "message": "can't enroll more than 5 students"}

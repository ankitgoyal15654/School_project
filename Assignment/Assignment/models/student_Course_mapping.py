from db import db
from .courses import Courses
from .users import Users


class StudentCourseMapping(db.Model):
    __tablename__ = 'student_course_mapping'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey(Users.id))
    course_id = db.Column(db.Integer, db.ForeignKey(Courses.id))

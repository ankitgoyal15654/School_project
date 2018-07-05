from db import db


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    student_enrolled = db.Column(db.Integer)
    is_active = db.Column(db.Boolean())
    created_datetime = db.Column(db.DateTime(), nullable=False)
    modified_datetime = db.Column(db.DateTime(), nullable=False)

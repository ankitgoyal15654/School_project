from db import db
from sqlalchemy_utils import JSONType


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16))
    role_id = db.Column(db.Integer)
    password = db.Column(db.String(16))
    first_name = db.Column(db.String(16))
    last_name = db.Column(db.String(16))
    father_name = db.Column(db.String(20))
    roll_no = db.Column(db.Integer)
    class_no = db.Column(db.String(11))
    address = db.Column(db.String(40))
    section = db.Column(db.String(100))
    admission_date = db.Column(db.Date())
    is_active = db.Column(db.Boolean())
    is_delete = db.Column(db.Boolean())
    modified_datetime = db.Column(db.DateTime(), nullable=False)

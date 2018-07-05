from models.users import Users
import logging
from db import db
from shared.responses import raise_exception
from sqlalchemy import and_
logger = logging.getLogger()
from datetime import datetime


def create_user(data):
    """
  {"data":{   "username" : "a123",
    "role_id" :"2",
    "password" : "12345",
    "first_name" : "12345",
    "last_name" : "12345",
    "father_name" : "12345",
    "roll_no" : "12334",
    "class_no" : "X",
    "address" : "12345",
    "section" : "12345",
    "admission_date" : "2017-01-01"}}
    To create the user
    """

    username = data["username"]
    role_id = data["role_id"]
    password = data["password"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    father_name = data["father_name"]
    roll_no = data["roll_no"]
    class_no = data["class_no"]
    address = data["address"]
    section = data["section"]
    admission_date = data["admission_date"]
    obj = Users(username=username, password=password,
                first_name=first_name, last_name=last_name, father_name=father_name,
                role_id=role_id,
                roll_no=roll_no, class_no=class_no,
                address=address, section=section, admission_date=admission_date,
                is_active=True, is_delete=False,
                modified_datetime=datetime.now())
    db.session.add(obj)
    db.session.commit()
    user_details = db.session.query(Users).filter_by(username=username).first()
    return{"id": user_details.id, "username": user_details.username}

from models.users import Users
import logging
from db import db
logger = logging.getLogger()
from . import role_details


def find_all_student(username):
    """
    To fetch all the students
    for admin only
    """
    role_detail = role_details.find_user_role(username)
    if role_detail["role_name"].lower() == 'admin':
        user_details = db.session.query(Users).filter_by(role_id=2).all()
        db.session.commit()
        students = []

        for user in user_details:
            result = {}
            result["id"] = user.id
            result["first_name"] = user.first_name
            result["last_name"] = user.last_name
            result["username"] = user.username
            result["address"] = user.address
            result["class"] = user.class_no
            result["section"] = user.section
            students.append(result)
        return students
    else:
        return {"message": "not for students"}

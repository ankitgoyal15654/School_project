from models.users import Users
from models.user_role import UserRole
import logging
from db import db
logger = logging.getLogger()


def find_user_role(username):
    """
    To get the role name for
    particular user
    """

    user_details = db.session.query(Users).filter_by(username=username).first()
    db.session.commit()
    role_id = user_details.role_id

    role_detail = db.session.query(UserRole).filter_by(id=role_id).first()
    response = {"role_name": role_detail.role_name}
    return response

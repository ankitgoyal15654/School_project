from models.users import Users
import logging
from db import db
logger = logging.getLogger()


def find_by_username(username):
    """
    To get the details of the username
    """

    user_details = db.session.query(Users).filter_by(username=username).first()
    db.session.commit()
    return user_details


def find_by_id(_id):
    """
    To get the details of user by id
    """
    return Users.query.filter_by(id=_id).first()

""" USER
Represent the table 'users' in database.
Using by SQLAlchemy ORM. """

# -*- coding: utf-8 -*-
# From Python 3
# From SQLAlchemy
from sqlalchemy import Column, String, Integer
# From Program
from backend.lib.base import Base


class User(Base):
    """ 'userID'         (int): user unique ID.
        'userName'       (str): user name.
        'userAvatarName' (str): user avatar name. """

    __tablename__ = 'users'

    userID = Column(Integer, primary_key=True)
    userName = Column(String(255))
    userAvatarName = Column(String(255))

    def __init__(self, user_name=None, avatar_name=None):
        self.userName = user_name
        self.userAvatarName = avatar_name

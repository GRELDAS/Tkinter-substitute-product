""" USER PRODUCTS
Represent the table 'userproducts' in database.
Using by SQLAlchemy ORM. """

# -*- coding: utf-8 -*-
# From Python 3
# From SQLAlchemy
from sqlalchemy import Column, String, Integer
# From Program
from backend.lib.base import Base


class UserProduct(Base):
    """ 'userProductID'        (int): user product unique ID.
        'userProductUserID'    (int): join - User ID.
        'userProductProductID' (int): join - Product ID. """

    __tablename__ = 'userproducts'

    userProductID = Column(Integer, primary_key=True)
    userProductUserID = Column(Integer)
    userProductProductID = Column(Integer)

    def __init__(
        self,
        user_id=None,
        product_id=None
    ):

        self.userProductUserID = user_id
        self.userProductProductID = product_id

""" CATEGORY
Represent the table 'categories' in database.
Using by SQLAlchemy ORM. """

# -*- coding: utf-8 -*-
# From Python 3
# From SQLAlchemy
from sqlalchemy import Column, String, Integer
# From Program
from backend.lib.base import Base


class Category(Base):
    """ 'categoryID'       (int): unique ID of category.
        'categoryProducts' (int): number of products of category.
        'categoryName'     (str): category name.
        'categoryIDOFF'    (str): category ID Open Food Fact. """

    __tablename__ = 'categories'

    categoryID = Column(Integer, primary_key=True)
    categoryProducts = Column(Integer)
    categoryName = Column(String(255))
    categoryIDOFF = Column(String(255))

    def __init__(
                self,
                category_products=None,
                name=None,
                category_id_off=None):
        self.categoryProducts = category_products
        self.categoryName = name
        self.categoryIDOFF = category_id_off

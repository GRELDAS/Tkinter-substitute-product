""" PRODUCT
Represent the table 'products' in database.
Using by SQLAlchemy ORM. """

# -*- coding: utf-8 -*-
# From Python 3
# From SQLAlchemy
from sqlalchemy import Column, String, Integer, Text
# From Program
from backend.lib.base import Base


class Product(Base):
    """ 'productID'             (int): product unique ID.
        'productName            (str): product name.
        'productURL'            (str): product Open Food facts URL.
        'productCreator'        (str): product creator.
        'productStore'          (str): product stores.
        'productNutriscore'     (str): product nutriscore.
        'productImgUrl'         (str): product image url.
        'productKcal'           (int): product Kcal value.
        'productKj'             (int): product Kj value.
        'productCategoryID'     (int): product category ID.
        'productSugar'          (int): product sugar quantity.
        'productBrand'          (str): product Brand. """

    __tablename__ = 'products'

    productID = Column(Integer, primary_key=True)
    productName = Column(String(255), default="empty")
    productUrl = Column(Text, default="empty")
    productCreator = Column(String(255), default="empty")
    productStore = Column(Text, default="empty")
    productNutriscore = Column(String(255))
    productImgUrl = Column(String(255), default="empty")
    productKcal = Column(Integer, default=0)
    productKj = Column(Integer, default=0)
    productCategoryID = Column(Integer)
    productSugar = Column(Integer, default=0)
    productBrand = Column(String(255), default="empty")

    def __init__(
        self,
        name=None,
        url=None,
        creator=None,
        stores=None,
        nutriscore=None,
        image_url=None,
        kcal=None,
        kj=None,
        category_id=None,
        sugar=None,
        brand=None
    ):

        self.productName = name
        self.productUrl = url
        self.productCreator = creator
        self.productStore = stores
        self.productNutriscore = nutriscore
        self.productImgUrl = image_url
        self.productKcal = kcal
        self.productKj = kj
        self.productCategoryID = category_id
        self.productSugar = sugar
        self.productBrand = brand

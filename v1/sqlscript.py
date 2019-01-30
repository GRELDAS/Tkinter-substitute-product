""" SQL CONSTRUCTOR
Construct the database purbeurre with SQL (without SQLAlchemy)
"""

# -*- coding: utf-8 -*-
import mysql.connector


class SqlConstructor():
    def __init__(self):
        # Attributes
        self.conn = None
        self.cursor = None
        # Methods initialized
        self.mysql_connection()
        self.create_database()
        self.mysql_db_connection()
        self.create_tables()

    def mysql_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vega3651@")
        self.cursor = self.conn.cursor()

    def mysql_db_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vega3651@",
            database="purbeurre")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # PRODUCTS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                produtID int NOT NULL AUTO_INCREMENT,
                productURL varchar(250),
                productStore varchar(250),
                productNutritionGrade varchar(10),
                productImgUrl varchar(250),
                productKcal int,
                productKj int,
                productCategoryID int,
                productSugar int,
                productBrand varchar(250),
                PRIMARY KEY(produtID)
            );
        """)
        # CATEGORIES TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                categoryID int NOT NULL AUTO_INCREMENT,
                categoryProducts int,
                categoryName varchar(250),
                categoryIDOFF varchar(250),
                productImgUrl varchar(250),
                PRIMARY KEY(categoryID)
            );
        """)
        # USER PRODUCTS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS userproducts (
                userProductID int NOT NULL AUTO_INCREMENT,
                userProductUserID int,
                userProductProductID int,
                PRIMARY KEY(userProductID)
            );
        """)
        # USERS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userID int NOT NULL AUTO_INCREMENT,
                userName varchar(250),
                userAvatarName varchar(250),
                PRIMARY KEY(userID)
            );
        """)

    def create_database(self):
        self.cursor.execute("CREATE DATABASE purbeurre")

    def mysql_close(self):
        self.conn.close()

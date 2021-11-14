#!/usr/bin/env python3
""" SQLAlchemy model named 'User' for a database table named 'users' """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
"""https://docs.sqlalchemy.org/en/13/orm/tutorial.html#create-a-schema"""


class User(Base):
    """ 'User' class (uses mysqlalchemy for
    declarative_base 'Base' object)
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

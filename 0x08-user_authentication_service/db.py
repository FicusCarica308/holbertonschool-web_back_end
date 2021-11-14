#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        [Summary]
        > Returns a User object that is simultaneously saved
        to the database

        Args:
            email (str): Email for the new user instance
            hashed_password (str): The new hashed password for the instance

        Returns:
            User: Returns a User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session
        self.__session.add(new_user)
        self.__session.commit()
        return new_user

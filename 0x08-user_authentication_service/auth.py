#!/usr/bin/env python3
""" module containing Authentication handling methods """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ returns a salted password hashed using bcrypt """
    bytes_password = bytes(password, 'utf-8')
    hashed_password = bcrypt.hashpw(bytes_password,  bcrypt.gensalt())
    return hashed_password


def _generate_uuid() -> str:
    """ returns a new random uuid """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Init """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Arugments:
                email(str): new user Email
                password(str): new user password
            [Summary]
            Creates a new User object and saves it to the database
            using the 'db' class from 'db.py'. If a User instance
            already exists the function does nothing.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates a given pair of credentials """
        try:
            user = self._db.find_user_by(email=email)
            result = bcrypt.checkpw(bytes(password, "utf-8"),
                                    user.hashed_password)
            if result is False:  # returns false when password doesnt match
                return False
            return True
        except NoResultFound:
            # runs if no user with given email is found
            return False

    def create_session(self, email: str) -> str:
        """ Adds a session id to a User object instance if it exists """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Gets the user instance associated with the given session_id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

#!/usr/bin/env python3
""" module containing Authentication handling methods """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ returns a salted password hashed using bcrypt """
    bytes_password = bytes(password, 'utf-8')
    hashed_password = bcrypt.hashpw(bytes_password,  bcrypt.gensalt())
    return hashed_password

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Init """
        self._db = DB()
        
    def register_user(self, email: str, password: str) -> User:
        """
            Temp comment
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user
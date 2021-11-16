#!/usr/bin/env python3
""" module containing Authentication handling methods """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns a salted password hashed using bcrypt """
    bytes_password = bytes(password, 'utf-8')
    hashed_password = bcrypt.hashpw(bytes_password,  bcrypt.gensalt())
    return hashed_password

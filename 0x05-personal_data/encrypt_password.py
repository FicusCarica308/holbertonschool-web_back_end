#!/usr/bin/env python3
"""
    Contains two functions that hash/validate passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a given password using bcrypt"""
    bytes_password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Checks if the given hashed password is the same as
    a given password (used to validate passwords)
    """
    bytes_password = bytes(password, 'utf-8')
    if bcrypt.checkpw(bytes_password, hashed_password):
        return True
    else:
        return False

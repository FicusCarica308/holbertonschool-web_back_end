#!/usr/bin/env python3
"""
    Contains two functions that hash/validate passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a given password using bcrypt"""
    byte_str = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(byte_str, bcrypt.gensalt())
    return hashed

#!/usr/bin/env python3
"""
passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypting passwords """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate that the provided password """
    return bcrypt.checkpw(password.encode(), hashed_password)

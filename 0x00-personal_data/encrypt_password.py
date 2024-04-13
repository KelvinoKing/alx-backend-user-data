#!/usr/bin/env python3
"""
User passwords should NEVER be stored in plain text in a database.
Implement a hash_password function that expects one string argument
name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


"""
Implement an is_valid function that expects 2 arguments and returns a boolean.
Arguments:
hashed_password: bytes type
password: string type
Use bcrypt to validate that the provided password matches the hashed password.
"""


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Returns a boolean"""
    return bcrypt.checkpw(password.encode(), hashed_password)

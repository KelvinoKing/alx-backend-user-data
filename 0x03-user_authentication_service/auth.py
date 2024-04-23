#!/usr/bin/env python3
"""
In this task you will define a _hash_password method
that takes in a password string arguments and returns bytes.
The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
The password should be encoded to base64 before hashing.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    _hash_password method that takes in a password string arguments
    and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
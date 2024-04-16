#!/usr/bin/env python3
"""
Create the class Auth:
in the file api/v1/auth/auth.py
import request from flask
class name Auth
public method
def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
that returns False - path and excluded_paths will be used later, now,
you don’t need to take care of them

public method
def authorization_header(self, request=None) -> str:
that returns None - request will be the Flask request object

public method def current_user(self, request=None) -> TypeVar('User'):
that returns None - request will be the Flask request object
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth method
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header method
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method
        """
        return None

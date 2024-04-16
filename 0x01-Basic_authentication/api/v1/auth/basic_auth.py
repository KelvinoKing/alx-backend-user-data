#!/usr/bin/env python3
"""
Create the class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """Extract base64 authorization header method
        """
        if authorization_header is None\
                or type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Decode base64 authorization header method
        Otherwise, return the decoded value as UTF8 string
        - you can use decode('utf-8')
        """
        if base64_authorization_header is None\
                or type(base64_authorization_header) is not str:
            return None
        try:
            decode_bytes = base64.b64decode(
                base64_authorization_header
            )
            decoded_str = decode_bytes.decode('utf-8')
            return decoded_str
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Add the method def extract_user_credentials(self,
        decoded_base64_authorization_header: str) -> (str, str)
        in the class BasicAuth that returns the user email and
        password from the Base64 decoded value.
        This method must return 2 values
        Return None, None if decoded_base64_authorization_header is None
        Return None, None if decoded_base64_authorization_header
        is not a string
        Return None, None if decoded_base64_authorization_header doesn’t
        contain :
        Otherwise, return the user email and the user password -
        these 2 values must be separated by a :
        You can assume decoded_base64_authorization_header will
        contain only one :
        """
        if decoded_base64_authorization_header is None\
                or type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(':')
        return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """
        Add the method def user_object_from_credentials(self,
        user_email: str, user_pwd: str) -> TypeVar('User')
        in the class BasicAuth that returns the User instance based
        on his email and password.
        If user_email or user_pwd is None, return None
        If no User instance found, return None
        """
        if user_email is None or user_pwd is None or\
                type(user_email) is not str or type(user_pwd) is not str:
            return None
        user = User.search({'email': user_email})
        if user == []:
            return None
        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

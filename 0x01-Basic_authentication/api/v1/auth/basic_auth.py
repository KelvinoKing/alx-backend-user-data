#!/usr/bin/env python3
"""
Create the class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64


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

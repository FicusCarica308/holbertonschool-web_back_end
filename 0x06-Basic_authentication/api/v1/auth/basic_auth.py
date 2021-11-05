#!/usr/bin/env python3
"""[summary]
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """[summary]
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
            Gets the base64 part of a authorization http header
            Format ( Basic [Base64] )
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        key_pair = authorization_header.split(' ')
        print(key_pair)
        if key_pair[0] != 'Basic':
            return None
        return key_pair[1]

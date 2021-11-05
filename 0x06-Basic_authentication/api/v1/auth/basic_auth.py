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
        if key_pair[0] != 'Basic':
            return None
        return key_pair[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
            Decodes a given base64 encoded string into a utf-8
            string
        """

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_str = base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        return decoded_str.decode('utf-8')

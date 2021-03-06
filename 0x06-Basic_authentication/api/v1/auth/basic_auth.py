#!/usr/bin/env python3
"""[summary]
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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
            return decoded_str.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
            gets user credentials from a deocded base 64 string
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_and_pass = decoded_base64_authorization_header.split(':', 1)
        return user_and_pass[0], user_and_pass[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """
            gets a user object from passed credentials
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        user = User()
        matching_objects = user.search({'email': user_email})

        if matching_objects is None or len(matching_objects) == 0:
            return None

        for object in matching_objects:
            if object.is_valid_password(user_pwd) is False:
                return None
            else:
                break
        return object

    def current_user(self, request=None) -> TypeVar('User'):
        """
        uses all class methods to find the current user we are
        signing into
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        extracted_base64 = self.extract_base64_authorization_header(
            auth_header)
        if extracted_base64 is None:
            return None
        decoded_base64 = self.decode_base64_authorization_header(
            extracted_base64)
        if decoded_base64 is None:
            return None
        extracted_creds = self.extract_user_credentials(
            decoded_base64)
        if extracted_creds is None:
            return None
        return self.user_object_from_credentials(extracted_creds[0],
                                                 extracted_creds[1])

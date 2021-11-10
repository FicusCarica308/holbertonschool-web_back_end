#!/usr/bin/env python3
"""[summary]
"""
from flask import request
from typing import List, TypeVar
from os import environ


class Auth():
    """
        [Summary]
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Determines if a given path is forbidden/unauthorized to a client
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        # Handle slashes at end of path / as well as values of excluded_paths
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        for current_path in excluded_paths:
            if '*' in current_path:
                if current_path.strip('*') in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            Finds out if the Authorization header argument
            is included in an http header

            request object from the flask module is passed
            (contains all http headers from client)
        """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Returns None 
        """
        return None
    
    def session_cookie(self, request=None):
        """ Returns a cookie from a request """
        if request is None:
            return None
        SESSION_NAME = environ.get('SESSION_NAME') # AKA name of cookie
        cookie = request.cookies.get(SESSION_NAME)
        return cookie

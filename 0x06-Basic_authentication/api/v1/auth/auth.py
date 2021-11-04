#!/usr/bin/env python3
"""[summary]
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """[summary]
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]

        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        # Handle slashes at end of path / as well as values of excluded_paths
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]

        Returns:
            [type]: [description]
        """
        return None

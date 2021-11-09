#!/usr/bin/env python3
""" Contains a class allowing this api
    to use session authentication
"""


from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Handles session id / session stortage"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a new session for a given user_id (base object id)"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        new_session_id = str(uuid4())
        self.user_id_by_session_id[new_session_id] = user_id
        return new_session_id

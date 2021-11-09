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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user_id using the session_id in user_id_by_session_id"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

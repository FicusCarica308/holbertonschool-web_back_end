#!/usr/bin/env python3
""" Main test file """
import requests


def register_user(email: str, password: str) -> None:
    r = requests.post('http://localhost:5000/users', data={'email': email, 'password': password})
    print(r.text)
    assert r.text.strip('\n') == {"email": email,"message":"user created"} and r.satus == 200
def log_in_wrong_password(email: str, password: str) -> None:
    pass
def log_in(email: str, password: str) -> str:
    pass
def profile_unlogged() -> None:
    pass
def profile_logged(session_id: str) -> None:
    pass
def log_out(session_id: str) -> None:
    pass
def reset_password_token(email: str) -> str:
    pass
def update_password(email: str, reset_token: str, new_password: str) -> None:
    pass

if __name__ == "__main__":
    register_user("manuelthemuffin@gmail.com", "12345")
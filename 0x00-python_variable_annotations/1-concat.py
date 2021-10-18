#!/usr/bin/env python3
"""
[summary]
Contains a single python function definition using Basic python
annotations
"""


def concat(str1: str, str2: str) -> str:
    """
    [summary]
    A type-annotated function concat that takes a string str1 and a string str2 as
    arguments and returns a concatenated string

    Args:
        str1 (str): first string to be concatenated
        str2 (str): second string to be concatenated
    Returns:
        str: final concatenated string (str1 + str2)
    """
    return str1 + str2

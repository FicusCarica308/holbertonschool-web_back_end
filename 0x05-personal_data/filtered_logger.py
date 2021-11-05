#!/usr/bin/env python3
"""[summary]
"""
from typing import List
from re import sub, search


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]"""
    for field in fields:
            message = sub(search("{0}=(.*?){1}".format(field, separator),
                                 message).group(1), redaction, message)
    return message

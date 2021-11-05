#!/usr/bin/env python3
"""[summary]
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]"""
    for field in fields:
        pattern = "(?<={}=).+?(?={})".format(field, separator)
        message = re.sub(pattern, redaction, message)
    return message

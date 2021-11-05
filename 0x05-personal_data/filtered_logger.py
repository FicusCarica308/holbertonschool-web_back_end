#!/usr/bin/env python3
"""[summary]
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]"""
    for field in fields:
            pattern = "{0}=(.*?){1}".format(field, separator)
            field_value = re.search(pattern, message)
            message = re.sub(field_value.group(1), redaction, message, 1)
    return message

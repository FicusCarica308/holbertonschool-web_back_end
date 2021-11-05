#!/usr/bin/env python3
"""[summary]
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]"""
    for field in fields:
            message = re.sub(re.search("{0}=(.*?){1}".format(field, separator),
                                 message).group(1), redaction, message)
    return message

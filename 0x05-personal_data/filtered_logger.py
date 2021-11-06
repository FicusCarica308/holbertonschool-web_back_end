#!/usr/bin/env python3
"""[summary]
"""
from typing import List
import re
import logging


PII_FIELDS = ("phone", "ssn", "password", "ip", "name")


def get_logger() -> logging.Logger:
    """ Creates a logger object with a custom formated StreamHandler"""
    log_obj = logging.Logger("user_data", level=logging.INFO)
    log_obj.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    log_obj.addHandler(stream)
    return log_obj

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]"""
    for field in fields:
        pattern = "(?<={}=).+?(?={})".format(field, separator)
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    """def format(self, record: logging.LogRecord) -> str:
        Formatter = logging.Formatter(self.FORMAT)
        record = Formatter.format(record)
        return filter_datum(self.fields, self.REDACTION, str(record).replace(
            self.SEPARATOR, self.SEPARATOR + ' '), self.SEPARATOR)"""

    def format(self, record: logging.LogRecord) -> str:
        """[summary]"""
        Formatter = logging.Formatter(self.FORMAT)
        record = Formatter.format(record)
        return filter_datum(self.fields, self.REDACTION,
                            str(record), self.SEPARATOR)

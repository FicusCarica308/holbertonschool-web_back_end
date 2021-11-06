#!/usr/bin/env python3
"""
    PII_FIELDS - This is a tuple that holds any fields
    we want obfuscated from any actions visible to
    outside sources
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("phone", "ssn", "password", "email", "name")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to a secure database
    using server environmental vairables
    """
    env_username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    env_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    env_hostName = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    env_dbName = os.environ.get("PERSONAL_DATA_DB_NAME")
    connector = mysql.connector.connect(user=env_username,
                                        password=env_password,
                                        database=env_dbName,
                                        host=env_hostName)
    return connector


def get_logger() -> logging.Logger:
    """ Creates a logger object with a custom formated StreamHandler"""
    log_obj = logging.getLogger("user_data")
    log_obj.setLevel(logging.INFO)
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

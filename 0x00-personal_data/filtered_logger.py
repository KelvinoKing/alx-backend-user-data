#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log
message obfuscated:
Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all
fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform
the substitution with a single regex.
"""

import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector import connection


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(r'{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message
                         )
    return message


"""
Update the class to accept a list of strings fields constructor argument.
Implement the format method to filter values in incoming log records using
filter_datum. Values for fields in fields should be filtered.
DO NOT extrapolate FORMAT manually. The format method should be less
than 5 lines long
"""


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format method"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


"""
Use user_data.csv for this task
Implement a get_logger function that takes no arguments and returns a
logging.Logger object.
The logger should be named "user_data" and only log up to logging.INFO level.
It should not propagate messages to other loggers.
It should have a StreamHandler
with RedactingFormatter as formatter.
Create a tuple PII_FIELDS constant at the root of the module containing
the fields from user_data.csv that are considered PII. PII_FIELDS can contain
only 5 fields - choose the right list of fields that can are
considered as “important” PIIs or information that you must hide in your logs.
Use it to parameterize the formatter."""


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


"""
Implement a get_db function that returns a connector to the database
(mysql.connector.connection.MySQLConnection object).
Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database
(pip3 install mysql-connector-python)
"""


def get_db() -> connection.MySQLConnection:
    """ Returns a connector to the database"""
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME', '')
    )

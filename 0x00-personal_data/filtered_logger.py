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

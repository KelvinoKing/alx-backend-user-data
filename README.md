```markdown
# 0x00. Personal Data

## Backend

### Authentification
 Weight: 1
 Ongoing second chance project - started Apr 10, 2024 6:00 AM, must end by Apr 14, 2024 6:00 AM
 Manual QA review must be done (request it when you are done with the project)
 An auto review will be launched at the deadline

**In a nutshell…**
 Manual QA review: In second deadline
 Auto QA review: 0.0/32 mandatory
 Altogether: waiting on some reviews

## Resources
Read or watch:
 [What Is PII, non-PII, and Personal Data?](#)
 [Logging Documentation](#)
 [bcrypt Package](#)
 [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
 Examples of Personally Identifiable Information (PII)
 How to implement a log filter that will obfuscate PII fields
 How to encrypt a password and check the validity of an input password
 How to authenticate to a database using environment variables

## Requirements
 All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
 All your files should end with a new line
 The first line of all your files should be exactly `#!/usr/bin/env python3`
 A `README.md` file, at the root of the folder of the project, is mandatory
 Your code should use the pycodestyle style (version 2.5)
 All your files must be executable
 The length of your files will be tested using wc
 All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
 All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
 All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
 A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
 All your functions should be type annotated

## Tasks

### 0. Regexing
Write a function called `filter_datum` that returns the log message obfuscated:

Arguments:
 `fields`: a list of strings representing all fields to obfuscate
 `redaction`: a string representing by what the field will be obfuscated
 `message`: a string representing the log line
 `separator`: a string representing by which character is separating all fields in the log line (message)

The function should use a regex to replace occurrences of certain field values.

`filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

```python
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
```

### 1. Log formatter
Copy the following code into `filtered_logger.py`.

```python
import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) > str:
        NotImplementedError
```

Update the class to accept a list of strings fields constructor argument.

Implement the format method to filter values in incoming log records using `filter_datum`. Values for fields in fields should be filtered.

### 2. Create logger
Use `user_data.csv` for this task.

Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object.

The logger should be named "user_data" and only log up to `logging.INFO` level. It should not propagate messages to other loggers. It should have a `StreamHandler` with `RedactingFormatter` as formatter.

Create a tuple `PII_FIELDS` constant at the root of the module containing the fields from `user_data.csv` that are considered PII. `PII_FIELDS` can contain only 5 fields  choose the right list of fields that are considered as “important” PIIs or information that you must hide in your logs.

### 3. Connect to secure database
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variables on the application server.

In this task, you will connect to a secure holberton database to read a `users` table. The database is protected by a username and password that are set as environment variables on the server named `PERSONAL_DATA_DB_USERNAME` (set the default as “root”), `PERSONAL_DATA_DB_PASSWORD` (set the default as an empty string) and `PERSONAL_DATA_DB_HOST` (set the default as “localhost”).

The database name is stored in `PERSONAL_DATA_DB_NAME`.

Implement a `get_db` function that returns a connector to the database (`mysql.connector.connection.MySQLConnection` object).

Use the `os` module to obtain credentials from the environment.

### 4. Read and filter data
Implement a `main` function that takes no arguments and returns nothing.

The function will obtain a database connection using `get_db` and retrieve all rows in the `users` table and display each row under a filtered format.

### 5. Encrypting passwords
User passwords should NEVER be stored in plain text in a database.

Implement a `hash_password` function that expects one string argument name `password` and returns a salted, hashed password, which is a byte string.

Use the `bcrypt` package to perform the hashing.

### 6. Check valid password
Implement an `is_valid` function that expects 2 arguments and returns a boolean.

Arguments:
 `hashed_password`: bytes type
 `password`: string type

Use `bcrypt` to validate that the provided password matches the hashed password.
```

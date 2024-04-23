# User Authentication Service

## Project Description
This project implements a user authentication service using Flask, SQLAlchemy, and bcrypt. It provides functionality for user registration, login, logout, profile management, password reset, and more.

## Learning Objectives
- Understanding API routes declaration in Flask
- Managing cookies for session management
- Retrieving request form data
- Handling various HTTP status codes
- Using SQLAlchemy for database interaction
- Implementing password hashing for security

## Requirements
- Allowed editors: vi, vim, emacs
- Code interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Code style: PEP 8 (pycodestyle)
- SQLAlchemy 1.3.x
- All files executable
- Proper documentation for modules, classes, and functions
- Type annotations for functions
- Flask app should interact only with Auth and not with DB directly
- Only public methods of Auth and DB should be used outside these classes

## Setup
Install bcrypt using:
```
pip3 install bcrypt
```

## Tasks Overview
1. **User Model**: Define a SQLAlchemy model named User with required attributes.
2. **Create User**: Implement adding a new user to the database.
3. **Find User**: Implement finding a user by specified criteria.
4. **Update User**: Implement updating user information.
5. **Hash Password**: Implement password hashing using bcrypt.
6. **Basic Flask App**: Set up a basic Flask app with a single route.
7. **Register User (Endpoint)**: Implement the endpoint to register a user.
8. **Credentials Validation**: Implement validation of login credentials.
9. **Generate UUIDs**: Implement a function to generate UUIDs.
10. **Get Session ID**: Implement creating a session for a user.
11. **Log In**: Implement login functionality.
12. **Find User by Session ID**: Implement finding a user by session ID.
13. **Destroy Session**: Implement destroying a user's session.
14. **Log Out**: Implement logout functionality.
15. **User Profile**: Implement fetching user profile information.
16. **Generate Reset Password Token**: Implement generating a reset password token.
17. **Get Reset Password Token (Endpoint)**: Implement the endpoint to get a reset password token.
18. **Update Password**: Implement updating a user's password.
19. **Update Password (Endpoint)**: Implement the endpoint to update a user's password.

For detailed instructions and code implementation, please refer to the respective files in the project repository.

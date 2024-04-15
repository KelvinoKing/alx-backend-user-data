# 0x01. Basic Authentication

## Background Context
In this project, you will learn about the authentication process and implement Basic Authentication on a simple API. While in industry it's recommended to use existing modules or frameworks for authentication (like Flask-HTTPAuth in Python-Flask), this project aims to provide a learning experience by implementing Basic Authentication from scratch.

## Resources
Read or watch:
- [REST API Authentication Mechanisms](https://www.restapitutorial.com/lessons/restapi-authentication.html)
- [Base64 in Python](https://docs.python.org/3/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://flask.palletsprojects.com/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements
### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.

## Tasks
### 0. Simple-basic-API
- Download and start the project from the provided archive.
- Setup and start the server.
- Use the API to test functionality.

### 1. Error handler: Unauthorized
- Implement a new error handler for status code 401.
- Test the error handler with a new endpoint.

### 2. Error handler: Forbidden
- Implement a new error handler for status code 403.
- Test the error handler with a new endpoint.

### 3. Auth class
- Create a class to manage API authentication.

### 4. Define which routes don't need authentication
- Update the Auth class method to define routes that don't need authentication.

### 5. Request validation!
- Validate all requests to secure the API.

### 6. Basic auth
- Create a class for Basic Authentication and integrate it into the app.

### 7. Basic - Base64 part
- Add a method to extract the Base64 part of the Authorization header.

### 8. Basic - Base64 decode
- Add a method to decode the Base64 Authorization header.

### 9. Basic - User credentials
- Add a method to extract user credentials from the decoded Base64 Authorization header.

### 10. Basic - User object
- Add a method to retrieve the User instance based on email and password.

### 11. Basic - Overload current_user - and BOOM!
- Implement a method to retrieve the User instance for a request using Basic Authentication.

---

**GitHub Repository:** [alx-backend-user-data](https://github.com/KelvinoKing/alx-backend-user-data)

**Directory:** 0x01-Basic_authentication

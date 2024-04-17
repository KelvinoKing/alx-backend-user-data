# 0x02. Session Authentication

## Table of Contents

- [Description](#description)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Et moi et moi et moi!](#0-et-moi-et-moi-et-moi)
  - [1. Empty session](#1-empty-session)
  - [2. Create a session](#2-create-a-session)
  - [3. User ID for Session ID](#3-user-id-for-session-id)
  - [4. Session cookie](#4-session-cookie)
  - [5. Before request](#5-before-request)
  - [6. Use Session ID for identifying a User](#6-use-session-id-for-identifying-a-user)
  - [7. New view for Session Authentication](#7-new-view-for-session-authentication)
  - [8. Logout](#8-logout)

## Description

This project focuses on implementing session authentication in a Flask application without using any external modules. Session authentication involves creating and managing user sessions using session IDs stored in cookies.

## Background Context

Session authentication is a common method used to manage user authentication in web applications. In this project, we'll implement session authentication from scratch, understanding the mechanisms involved in creating and managing user sessions.

## Resources

- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=-RCnNyD0L-s)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask Cookie](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Response.set_cookie)

## Learning Objectives

By the end of this project, you should be able to:

- Understand authentication mechanisms in RESTful APIs
- Implement session authentication in a Flask application
- Manage user sessions using session IDs stored in cookies

## Requirements

- All scripts will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Code must follow PEP 8 style guidelines
- Code should use the `pycodestyle` style (version 2.5)
- All files must be executable
- Documentation is mandatory for all classes and functions
- Documentation should follow a specific format and length

## Tasks

### 0. Et moi et moi et moi!

Copy all your work from the 0x06. Basic authentication project into this new folder. Additionally, implement a new endpoint: `GET /users/me` to retrieve the authenticated User object.

### 1. Empty session

Create a `SessionAuth` class inheriting from `Auth`. For now, leave the class empty to ensure proper inheritance and validate the switch using environment variables.

### 2. Create a session

Update the `SessionAuth` class to include functionality for creating session IDs for user authentication. Implement a method `create_session(self, user_id: str = None) -> str` to generate session IDs.

### 3. User ID for Session ID

Expand the `SessionAuth` class to include a method `user_id_for_session_id(self, session_id: str = None) -> str` to retrieve User IDs based on session IDs.

### 4. Session cookie

Add a method `session_cookie(self, request=None)` to the `Auth` class to extract session ID from cookies in the request.

### 5. Before request

Update the `@app.before_request` method in `api/v1/app.py` to handle session authentication. Exclude the `/api/v1/auth_session/login/` path and ensure proper authentication for other routes.

### 6. Use Session ID for identifying a User

Update the `SessionAuth` class with a method `current_user(self, request=None)` to retrieve User instances based on session IDs.

### 7. New view for Session Authentication

Create a new Flask view `POST /auth_session/login` to handle authentication using session IDs.

### 8. Logout

Implement a `destroy_session` method in the `SessionAuth` class to handle user logout by deleting session IDs.

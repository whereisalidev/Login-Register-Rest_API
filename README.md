# Login and Register REST API with JWT Token

Introducing User Authentication APIs (login and register) with validation logic built in Django Rest Framework.

## Features

- User registration
- User login
- JWT token generation

## API Endpoints

### Register a New User

**URL:** `/api/register/`
**Method:** `POST`

### Login User

**URL:** `/api/login/`
**Method:** `POST`

**Request Body:**
```bash
#Register user:
{
    "username": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "integer"
}

# Login user:
{
    "email": "string",
    "password": "integer"
}


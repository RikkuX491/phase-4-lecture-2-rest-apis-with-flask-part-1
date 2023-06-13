# Phase 4, Lecture 2: Rest APIs with Flask (Part 1)

## Lecture Topics

- Handling POST requests
- Rest APIs with Flask (GET and POST requests)

## Important Definitions

- Representational State Transfer (REST): a convention for developing applications that use HTTP in a consistent, human-readable, machine-readable way.
- Application Programming Interface (API): a software application that allows two or more software applications to communicate with one another.
- GET: the most common HTTP request method. Signifies that the client is attempting to view the located resource.
- POST: the second most common HTTP request method. Signifies that the client is attempting to submit a form to create a new resource.

## Introduction

In today's lecture, we will add functionality to our Flask app to handle POST requests. We will also discuss about REST APIs with Flask.

## Setup

1. Fork and then Clone this repository.

2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required libraries.

3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

4. Enter the command `cd server` in the terminal to move into the server directory.

5. Run these commands in the terminal (make sure that you are in the `server` directory before running these terminal commands):

```py
export FLASK_APP=app.py

export FLASK_RUN_PORT=7000
```

6. We will write code in the `app.py` file to build functionality to handle POST requests to the `/hotels` route.

7. We will rewrite the code for handling GET and POST requests such that it follows the convention for REST APIs.

8. Enter the command `flask run` or `python app.py` to run the Flask app.

9. We will use Postman to test our app's functionality for handling GET and POST requests.
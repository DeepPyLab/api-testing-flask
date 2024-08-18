# API Testing with Flask

## Overview

This project demonstrates how to build and test a basic RESTful API using Flask, a lightweight Python web framework. It includes both unit and integration tests to ensure the API functions as expected. The code adheres to best practices in Python development, including linting with `pylint` and formatting with `black`.

## Project Structure

api-testing-flask/
├── app/
│ ├── init.py
│ └── routes.py
├── tests/
│ └── test_routes.py
├── .github/
│ └── workflows/
│ └── python-app.yml
├── .pylintrc
├── requirements.txt
├── README.md
└── .gitignore


- **app/**: Contains the Flask application code.
- **tests/**: Contains the test cases for the API.
- **.github/workflows/python-app.yml**: GitHub Actions workflow for CI/CD.
- **.pylintrc**: Configuration for `pylint`.
- **requirements.txt**: Lists project dependencies.
- **README.md**: This file.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/DeepPyLab/api-testing-flask.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd api-testing-flask
    ```

3. **Set Up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Flask application locally:
```bash
python app/routes.py
```

**Running Tests**

**To run unit and integration tests:**

```bash
pytest --cov=app --cov-report=term-missing
```

**Code Quality**

**Linting: Code is linted using pylint. To run pylint:**

```bash
pylint app tests
```

**Formatting: Code is formatted using black. To format code:**

```bash
black app tests
```

**Continuous Integration**

This project uses GitHub Actions for continuous integration. The CI workflow runs tests and checks code quality on each commit. The configuration can be found in .github/workflows/python-app.yml.

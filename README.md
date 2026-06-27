# My DevOps Project

A simple Flask-based DevOps practice project.

## Features

- Flask web application
- Health check endpoint
- Info endpoint
- Pytest test suite
- Flake8 linting
- GitHub Actions CI pipeline

## Project Structure

    my-devops-project/
    ├── src/
    │   └── app.py
    ├── tests/
    │   └── test_app.py
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── requirements.txt
    ├── .gitignore
    ├── .flake8
    └── README.md

## Setup

### 1. Clone the repository

    git clone https://github.com/Alibras257/my-devops-project.git
    cd my-devops-project

### 2. Create and activate a virtual environment

#### Windows

    python -m venv venv
    venv\Scripts\activate

#### Mac/Linux

    python3 -m venv venv
    source venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

## Run the Application

    python src/app.py

The app will start on:

    http://127.0.0.1:5000

## Available Endpoints

- `/` - Home endpoint
- `/health` - Health check
- `/info` - App info

## Run Tests

    python -m pytest

## Run Linting

    python -m flake8 src tests

## CI Pipeline

GitHub Actions automatically runs:
- linting
- tests

on every push and pull request to `main`.

## Author

Built by Alibras

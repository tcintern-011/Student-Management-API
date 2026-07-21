# Student & Book Management API

A simple RESTful CRUD API built with **FastAPI** for managing **students** and **books**. The project demonstrates core FastAPI concepts including routing, request validation with Pydantic, response models, HTTP status codes, and exception handling.

Data is stored **in memory**, making this project ideal for learning, prototyping, and testing FastAPI applications.

---

# Features

## Student Management

* List all students
* Retrieve a student by ID
* Create a new student
* Update an existing student
* Delete a student

## Book Management

* List all books
* Retrieve a book by ID
* Update an existing book
* Delete a book

## Additional Features

* Request validation using **Pydantic**
* Automatic response validation with `response_model`
* Proper HTTP status codes
* Custom error handling using `HTTPException`
* Interactive API documentation (Swagger UI & ReDoc)

---

# Technologies Used

* Python 3.8+
* FastAPI
* Pydantic
* Uvicorn

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Navigate to the project folder:

```bash
cd your-repository
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The `--reload` flag automatically restarts the server whenever code changes are detected.

---

# API URLs

Application:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Data Models

## Student

| Field  | Type    | Validation           |
| ------ | ------- | -------------------- |
| id     | Integer | Auto-generated       |
| name   | String  | 2–50 characters      |
| age    | Integer | 1–100                |
| course | String  | Minimum 2 characters |

---

## Book

| Field  | Type    | Validation            |
| ------ | ------- | --------------------- |
| id     | Integer | Required              |
| name   | String  | 10–100 characters     |
| author | String  | 10–100 characters     |
| isbn   | String  | Exactly 13 characters |
| genre  | String  | 2–20 characters       |

---

# API Endpoints

## Student Endpoints

| Method | Endpoint                 | Description              | Status |
| ------ | ------------------------ | ------------------------ | ------ |
| GET    | `/students`              | Retrieve all students    | 200    |
| GET    | `/students/{student_id}` | Retrieve a student by ID | 200    |
| POST   | `/students`              | Create a new student     | 201    |
| PUT    | `/students/{student_id}` | Update a student         | 200    |
| DELETE | `/students/{student_id}` | Delete a student         | 204    |

---

## Book Endpoints

| Method | Endpoint           | Description           | Status |
| ------ | ------------------ | --------------------- | ------ |
| GET    | `/books`           | Retrieve all books    | 200    |
| GET    | `/books/{book_id}` | Retrieve a book by ID | 200    |
| PUT    | `/books/{book_id}` | Update a book         | 200    |
| DELETE | `/books/{book_id}` | Delete a book         | 204    |

> **Note:** All endpoints that retrieve, update, or delete a single resource return **404 Not Found** if the requested ID does not exist.

---

# Example Requests

## Create Student

**POST**

```
/students
```

Request Body

```json
{
    "name": "Sara",
    "age": 20,
    "course": "Data Science"
}
```

---

## Update Student

**PUT**

```
/students/1
```

Request Body

```json
{
    "name": "Ali Khan",
    "age": 22,
    "course": "Computer Science"
}
```

---

## Get All Books

**GET**

```
/books
```

---

## Get Book by ID

**GET**

```
/books/1
```

---

## Update Book

**PUT**

```
/books/1
```

Request Body

```json
{
    "id": 1,
    "name": "English Literature",
    "author": "Yaseen Ahmed",
    "isbn": "1234567891012",
    "genre": "Literature"
}
```

---

## Delete Book

**DELETE**

```
/books/1
```

---

# Validation

FastAPI and Pydantic automatically validate incoming requests.

Examples include:

* Student name must be between **2 and 50 characters**
* Student age must be between **1 and 100**
* Book name must be between **10 and 100 characters**
* Author name must be between **10 and 100 characters**
* ISBN must contain exactly **13 characters**
* Genre must contain between **2 and 20 characters**

If validation fails, FastAPI automatically returns a **422 Unprocessable Entity** response with detailed validation errors.

---

# Project Structure

```
.
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```


For POST and PUT, send the body as JSON with `Content-Type: application/json`.

You can test all of these directly in the browser via the interactive docs at `/docs`, or with a tool like Postman/Insomnia.

```


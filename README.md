Student Management API

A simple CRUD API built with FastAPI for managing student records (name, age, course). Data is stored in memory, making this ideal for learning, prototyping, or testing.

Features
List all students
Get a single student by ID
Add a new student
Update an existing student's details
Delete a student
Automatic request validation via Pydantic (e.g. name length, age range)
Interactive API docs (Swagger UI) included out of the box
Requirements
Python 3.8+
FastAPI
Uvicorn (ASGI server)

Install all dependencies at once using the included requirements.txt file:

bash
pip install -r requirements.txt

This file lists the exact packages needed to run the project (fastapi and uvicorn[standard]), so anyone setting up the project — or any hosting platform like Render — can install them with a single command instead of installing each package manually.

Running the API
bash
uvicorn main:app --reload

The --reload flag enables auto-restart on code changes (useful during development).

Once running, the API is available at:

App: http://127.0.0.1:8000
Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
Alternative docs (ReDoc): http://127.0.0.1:8000/redoc
Data Model
Field	Type	Rules
id	int	Auto-assigned, not user-provided
name	string	2–50 characters
age	int	1–100
course	string	Minimum 2 characters
Endpoints
Method	Endpoint	Description	Success Status
GET	/students	Get all students	200
GET	/students/{id}	Get a student by ID	200
POST	/students	Create a new student	201
PUT	/students/{id}	Update a student by ID	200
DELETE	/students/{id}	Delete a student by ID	204

All single-student endpoints return 404 Not Found if the given id doesn't exist.

Example URLs

Get all students

GET http://127.0.0.1:8000/students

Get a student by ID

GET http://127.0.0.1:8000/students/1

Create a student

POST http://127.0.0.1:8000/students
Body: {"name": "Sara", "age": 20, "course": "Data Science"}

Update a student

PUT http://127.0.0.1:8000/students/1
Body: {"name": "Ali Khan", "age": 22, "course": "Computer Science"}

Delete a student

DELETE http://127.0.0.1:8000/students/1

For POST and PUT, send the body as JSON with Content-Type: application/json.

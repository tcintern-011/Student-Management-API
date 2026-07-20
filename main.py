from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="Student Management API"
)
class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=2)


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=2)

students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 21,
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Ahmed",
        "age": 22,
        "course": "Software Engineering"
    }
]

@app.get("/students", response_model=List[Student])
def get_students():
    return students


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def add_student(student: StudentCreate):

    new_id = max([s["id"] for s in students], default=0) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    students.append(new_student)

    return new_student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: StudentCreate):

    for student in students:

        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
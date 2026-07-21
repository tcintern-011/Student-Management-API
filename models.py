from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=2)


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=2)

class Book(BaseModel):
    id : int
    name: str = Field(..., min_length=10, max_length=100)
    author: str = Field(..., min_length = 10 , max_length = 100)
    isbn: str = Field(..., min_length = 13, max_length = 13)
    genre:str = Field(..., min_length = 2 , max_length= 20)
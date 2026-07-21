from fastapi import FastAPI, HTTPException, status
from models import StudentCreate, Student, Book


app = FastAPI(
    title="Student Management API")
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

all_books = [
    {
        "id" : 1,
        "name" : "english Literature", 
        "author" : "yaseen Ahmed", 
        "isbn" : "1234567891012",
        "genre" : "Literature"
    }, 
    {
        "id" : 2,
        "name" : "Linear Algebra Problems", 
        "author" : "Ibrahim Raza", 
        "isbn" : "1234567891014", 
        "genre" : "Maths"
        
    },
]

@app.get("/students", response_model=list[Student])
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
    
    
@app.get("/books", response_model= list[Book])
def get_all_books():
    return all_books

app.get("/books/{book_id}" , response_model = Book)
def get_book(book_id: int):
    for book in all_books:
        
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Book Not Found"
    )
    
@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(book_id: int):

    for index, book in enumerate(all_books):

        if book["id"] == book_id:
            all_books.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found"
    )

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):

    for b in all_books:

        if b["id"] == book_id:

            b["name"] = updated_book.name
            b["author"] = updated_book.author
            b["genre"] = updated_book.genre
            b["isbn"] = updated_book.isbn
            
            return b

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Boook Not Found"
    )
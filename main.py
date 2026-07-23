from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import BookModel, UserModel
from schema import Book, BookCreate, UserCreate, UserOut, Token, StudentCreate, Student
from security import hash_password, verify_password, create_access_token, get_current_user






Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student Management API")
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

# all_books = [
#     {
#         "id" : 1,
#         "name" : "english Literature", 
#         "author" : "yaseen Ahmed", 
#         "isbn" : "1234567891012",
#         "genre" : "Literature"
#     }, 
#     {
#         "id" : 2,
#         "name" : "Linear Algebra Problems", 
#         "author" : "Ibrahim Raza", 
#         "isbn" : "1234567891014", 
#         "genre" : "Maths"
        
#     },
# ]


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
    
    
@app.post("/signup", response_model=UserOut, status_code=201)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = UserModel(
        username=user.username,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    
@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token)

    
@app.post("/book", response_model = Book, status_code = 201)
def add_book(book: BookCreate,db: Session = Depends(get_db) ):
    existingbook = (db.query(BookModel).filter(BookModel.isbn == book.isbn)
    .first())
    
    if existingbook: 
        raise HTTPException(
            status_code = 400, 
            detail = "Book with this Isbn already exists"
        )
    new_book = BookModel(
        name = book.name, 
        author = book.author, 
        isbn = book.isbn, 
        genre = book.genre
    )
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
    
    
@app.get("/books", response_model= list[Book])
def get_all_books(db: Session = Depends(get_db)):
    all_books = db.query(BookModel).all()
    return all_books

@app.get("/books/{book_id}" , response_model = Book)
def get_book(book_id: int,db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Book Not Found"
        )
    return book



# THIS IS ONLY THE PROTECTED ROUTE FOR THE CURRENT TASK
@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),  
):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Book Not Found"
        )
    db.delete(book)
    db.commit()


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "Book Not Found"
        )
    

    book.name = updated_book.name
    book.author = updated_book.author
    book.isbn = updated_book.isbn
    book.genre = updated_book.genre

    db.commit()
    db.refresh(book)
    return book

    
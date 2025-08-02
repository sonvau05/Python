from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

class Student(BaseModel):
    id: UUID | None = None
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=150)
    class_name: str = Field(..., min_length=1, max_length=50)

students_db: List[Student] = []

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    student.id = uuid4()
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return students_db

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: UUID):
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail={"error": "Student not found"})

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: UUID, updated_student: Student):
    for i, student in enumerate(students_db):
        if student.id == student_id:
            updated_student.id = student_id
            students_db[i] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail={"error": "Student not found"})

@app.delete("/students/{student_id}")
async def delete_student(student_id: UUID):
    for i, student in enumerate(students_db):
        if student.id == student_id:
            students_db.pop(i)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail={"error": "Student not found"})

@app.get("/students/search/", response_model=List[Student])
async def search_students(name: str | None = None, class_name: str | None = None, age: int | None = None):
    results = students_db
    if name:
        results = [s for s in results if name.lower() in s.name.lower()]
    if class_name:
        results = [s for s in results if class_name.lower() in s.class_name.lower()]
    if age:
        results = [s for s in results if s.age == age]
    return results
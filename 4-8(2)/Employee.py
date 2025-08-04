from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

DATABASE_URL = "mysql+pymysql://root:password@localhost/employee_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class EmployeeDB(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50))
    birthday = Column(Date)
    phone = Column(String(15))
    email = Column(String(100))

Base.metadata.create_all(bind=engine)

class Employee(BaseModel):
    id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str
    birthday: date
    phone: str
    email: str

app = FastAPI()

@app.post("/employees/")
async def create_employee(employee: Employee):
    db = SessionLocal()
    db_employee = EmployeeDB(**employee.dict(exclude_unset=True))
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    db.close()
    return db_employee

@app.get("/employees/")
async def read_employees():
    db = SessionLocal()
    employees = db.query(EmployeeDB).all()
    db.close()
    return employees

@app.get("/employees/{employee_id}")
async def read_employee(employee_id: int):
    db = SessionLocal()
    employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    db.close()
    if employee is None:
        raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
    return employee

@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    db = SessionLocal()
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if db_employee is None:
        db.close()
        raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
    for key, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    db.close()
    return db_employee

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    db = SessionLocal()
    employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if employee is None:
        db.close()
        raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
    db.delete(employee)
    db.commit()
    db.close()
    return {"message": "Nhân viên đã được xóa"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
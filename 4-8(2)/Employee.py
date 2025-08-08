from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData
from datetime import date

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/employee_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

employees = Table(
    "employees", metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50)),
    Column("middle_name", String(50), nullable=True),
    Column("last_name", String(50)),
    Column("birthday", Date),
    Column("phone", String(15)),
    Column("email", String(100))
)
metadata.create_all(engine)

class Employee(BaseModel):
    id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str
    birthday: date
    phone: str
    email: str

app = FastAPI()

@app.post("/employees/", response_model=Employee)
async def create_employee(employee: Employee):
    with engine.connect() as conn:
        result = conn.execute(employees.insert().values(**employee.dict(exclude_unset=True)))
        conn.commit()
        return {**employee.dict(), "id": result.inserted_primary_key[0]}

@app.get("/employees/", response_model=list[Employee])
async def read_employees():
    with engine.connect() as conn:
        result = conn.execute(employees.select())
        return [dict(row) for row in result]

@app.get("/employees/{employee_id}", response_model=Employee)
async def read_employee(employee_id: int):
    with engine.connect() as conn:
        result = conn.execute(employees.select().where(employees.c.id == employee_id))
        row = result.first()
        if row is None:
            raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
        return dict(row)

@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee: Employee):
    with engine.connect() as conn:
        result = conn.execute(employees.select().where(employees.c.id == employee_id))
        if result.first() is None:
            raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
        conn.execute(employees.update().where(employees.c.id == employee_id).values(**employee.dict(exclude_unset=True)))
        conn.commit()
        return {**employee.dict(), "id": employee_id}

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    with engine.connect() as conn:
        result = conn.execute(employees.select().where(employees.c.id == employee_id))
        if result.first() is None:
            raise HTTPException(status_code=404, detail="Nhân viên không tìm thấy")
        conn.execute(employees.delete().where(employees.c.id == employee_id))
        conn.commit()
        return {"message": "Nhân viên đã được xóa"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
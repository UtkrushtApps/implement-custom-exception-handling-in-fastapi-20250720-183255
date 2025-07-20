from fastapi import FastAPI
from routers import employees, departments

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(departments.router, prefix="/departments", tags=["departments"])

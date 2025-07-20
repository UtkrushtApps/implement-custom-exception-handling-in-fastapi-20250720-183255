from pydantic import BaseModel

class EmployeeRead(BaseModel):
    id: int
    name: str
    email: str
    department_id: int

    class Config:
        from_attributes = True

class DepartmentRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

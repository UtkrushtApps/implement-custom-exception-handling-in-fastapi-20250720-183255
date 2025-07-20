from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_async_session
from models import Employee
from schemas import EmployeeRead

router = APIRouter()

@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Employee).where(Employee.id == employee_id))
    employee = result.scalar_one_or_none()
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee

from fastapi import APIRouter
from schemas import DepartmentRead

router = APIRouter()

@router.get("/", response_model=list[DepartmentRead])
async def list_departments():
    # Placeholder for demonstration
    return []

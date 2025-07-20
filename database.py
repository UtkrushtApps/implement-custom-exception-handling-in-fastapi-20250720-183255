import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://hr_user:hr_pass@localhost:5432/hr_db")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_async_session():
    async with async_session() as session:
        yield session

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.core.config import settings

async_engine = create_async_engine(
    settings.database_url,
    echo=True,
    future=True
)


AsyncSessionLocal = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

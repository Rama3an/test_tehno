from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models import MaterialTable


class CalcRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        return cls._instance

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save_cost_db(self, total_cost: float) -> None:
        result = MaterialTable(total_cost_rub=total_cost)
        self.db.add(result)
        await self.db.commit()

    async def get_data_db(self, query: str):
        query = text(query)
        return await self.db.execute(query)

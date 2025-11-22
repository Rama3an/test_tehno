from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.materials import MaterialsRequest
from src.db.session import get_async_db
from src.db.repository import CalcRepository
from src.services.calc_materials import sum_materials

router = APIRouter()


@router.post("/calc")
async def calc_request(
        data: MaterialsRequest,
        db: AsyncSession = Depends(get_async_db)
):
    total_cost = sum_materials(data)
    db_conn = CalcRepository(db)
    await db_conn.save_cost_db(total_cost)

    return {"total_cost_rub": total_cost}


@router.get("/sort_materials")
async def get_sort_materials(db: AsyncSession = Depends(get_async_db)):
    db_conn = CalcRepository(db)
    query = """
    select total_cost_rub, created_at from calc_results
    ORDER BY created_at
    LIMIT 10
    """
    result_sql = await db_conn.get_data_db(query)
    result_data = [
        {"total_cost_rub": t_sum, "create_at": time} for t_sum, time in result_sql.all()
    ]
    return result_data


@router.get("/health")
async def get_health(db: AsyncSession = Depends(get_async_db)):
    try:
        db_conn = CalcRepository(db)
        query = """
        select 1
        """
        await db_conn.get_data_db(query)
    except Exception:
        return {"Error": 500}
    else:
        return {"OK": 200}
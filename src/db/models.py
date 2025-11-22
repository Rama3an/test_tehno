from sqlalchemy import Column, Integer, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MaterialTable(Base):
    __tablename__ = "calc_results"

    id = Column(Integer, primary_key=True, index=True)
    total_cost_rub = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from pydantic import BaseModel, Field, validator
from typing import List


class Material(BaseModel):
    name: str = Field(..., min_length=1)
    qty: float = Field(..., gt=0)
    price_rub: float = Field(..., ge=0)

    @validator("name")
    def normalize_name(cls, v: str) -> str:
        return v.strip().lower()


class MaterialsRequest(BaseModel):
    materials: List[Material]
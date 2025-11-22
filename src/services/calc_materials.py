from src.schemas.materials import MaterialsRequest


def sum_materials(data: MaterialsRequest) -> int:
    total_cost = 0
    for value in data.materials:
        total_cost += value.price_rub
    return total_cost

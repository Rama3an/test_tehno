from fastapi import FastAPI
from src.api.v1.material import router as router_v1

app = FastAPI()


app.include_router(router_v1, prefix="/api/v1")
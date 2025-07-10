from fastapi import FastAPI
# from app.api.v1 import user  # подставим свои роуты позже

app = FastAPI(
    title="Alchemy App",
    version="1.0.0"
)

# Подключаем маршруты
# app.include_router(user.router, prefix="/api/v1", tags=["users"])
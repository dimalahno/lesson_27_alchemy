import uvicorn
from fastapi import FastAPI

from app.api import author

app = FastAPI(
    title="Alchemy App",
    version="1.0.0"
)

# Подключаем маршруты
app.include_router(author.router, prefix="/api/v1", tags=["authors"])

# ✅ Запуск из файла: `python app/main.py`
if __name__ == "__main__":
    print(f"Swagger: http://127.0.0.1:8000/docs")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
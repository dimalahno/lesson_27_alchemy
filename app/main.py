import uvicorn
from fastapi import FastAPI

from app.api import author, book, user

app = FastAPI(
    title="Alchemy App",
    version="1.0.0"
)

# Подключаем маршруты
app.include_router(author.router, prefix="/api/v1", tags=["authors"])
app.include_router(book.router, prefix="/api/v1", tags=["books"])
app.include_router(user.router, prefix="/api/v1", tags=["users"])


if __name__ == "__main__":
    print(f"Swagger: http://127.0.0.1:8000/docs")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
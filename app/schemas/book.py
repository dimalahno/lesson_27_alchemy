from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author_id: int

class BookRead(BaseModel):
    id: int
    title: str
    author_id: int

    # позволяет Pydantic конвертировать ORM-модели (Book) в схемы
    # обязательно для работы с SQLAlchemy
    class Config:
        orm_mode = True
from typing import List
from pydantic import BaseModel
from app.schemas.book import BookRead


class AuthorCreate(BaseModel):
    name: str


class AuthorRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class AuthorReadWithBooks(AuthorRead):
    books: List[BookRead] = []
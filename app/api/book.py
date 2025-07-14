from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.repositories.book_repository import BookRepository
from app.schemas.book import BookCreate, BookRead

router = APIRouter()


@router.post("/books", response_model=BookRead)
async def create_book(book_data: BookCreate, db: AsyncSession = Depends(get_db)):
    repo = BookRepository(db)
    return await repo.add_book(book_data)


@router.get("/authors/{author_id}/books", response_model=list[BookRead])
async def get_books_by_author(author_id: int, db: AsyncSession = Depends(get_db)):
    repo = BookRepository(db)
    return await repo.get_books_by_author_id(author_id)


@router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    repo = BookRepository(db)
    await repo.delete_book_by_id(book_id)

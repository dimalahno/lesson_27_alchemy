from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.models.book import Book
from app.schemas.book import BookCreate

class BookRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_book(self, book_data: BookCreate) -> Book:
        new_book = Book(title = book_data.title, author_id = book_data.author_id)
        self.session.add(new_book)
        await self.session.commit()
        await self.session.refresh(new_book)
        return new_book

    async def get_books_by_author_id(self, author_id: int) -> list[Book]:
        stmt = select(Book).where(Book.author_id == author_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete_book_by_id(self, book_id: int) -> None:
        stmt = delete(Book).where(Book.id == book_id)
        await self.session.execute(stmt)
        await self.session.commit()
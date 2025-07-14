from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from app.models.author import Author

class AuthorService:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def get_author_lazy(self, author_id: int) -> Author | None:
        stmt = (select(Author)
        .options(selectinload(Author.books))
        .where(Author.id == author_id))
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_author_eager(self, author_id: int) -> Author | None:
        stmt = (select(Author)
                .options(joinedload(Author.books))
                .where(Author.id == author_id))
        result = await self.session.execute(stmt)
        return result.unique().scalar_one_or_none()


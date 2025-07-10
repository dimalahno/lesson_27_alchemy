from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.models.author import Author
from app.schemas.author import AuthorCreate

class AuthorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_author(self, author_data: AuthorCreate) -> Author:
        author = Author(name=author_data.name)
        self.session.add(author)
        await self.session.commit()
        await self.session.refresh(author)
        return author

    async def get_all_authors(self) -> list[Author]:
        result = await self.session.execute(select(Author))
        return result.scalars().all()

    async def delete_author_by_id(self, author_id: int) -> None:
        await self.session.execute(
            delete(Author).where(Author.id == author_id)
        )
        await self.session.commit()
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.repositories.author_repository import AuthorRepository
from app.schemas.author import AuthorCreate, AuthorRead, AuthorReadWithBooks
from app.services.author_service import AuthorService

router = APIRouter()

@router.post("/author", response_model=AuthorRead)
async def create_author(author_data: AuthorCreate, db: AsyncSession = Depends(get_db)):
    repo = AuthorRepository(db)
    return await repo.add_author(author_data)


@router.get("/authors", response_model=list[AuthorRead])
async def get_all_authors(db: AsyncSession = Depends(get_db)):
    repo = AuthorRepository(db)
    return await repo.get_all_authors()


@router.get("/authors/{author_id}", response_model=AuthorReadWithBooks)
async def get_author(author_id: int, eager: bool = False, db: AsyncSession = Depends(get_db)):
    service = AuthorService(db)
    author = await (
        service.get_author_eager(author_id)
        if eager else
        service.get_author_lazy(author_id)
    )

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author


@router.delete("/authors/{author_id}", status_code=204)
async def delete_author(author_id: int, db: AsyncSession = Depends(get_db)):
    repo = AuthorRepository(db)
    await repo.delete_author_by_id(author_id)
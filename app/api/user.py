from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users/transaction-test")
async def test_user_transaction(db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    await service.create_users_with_rollback_demo()
    return {"status": "тест завершён"}

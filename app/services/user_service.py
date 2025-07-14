from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.user import User

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    # !!! Ошибка: username дублируется, т.к оно уникально
    async def create_users_with_rollback_demo(self):
        try:
            async with self.session.begin():  # транзакция
                self.session.add_all([
                    User(username="alice", email="alice@example.com"),
                    User(username="bob", email="bob@example.com"),
                    User(username="alice", email="duplicate@example.com")
                ])
        except IntegrityError:
            await self.session.rollback()
            print("Откат выполнен из-за ошибки уникальности.")

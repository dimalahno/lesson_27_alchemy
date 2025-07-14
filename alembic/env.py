import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context

import os
from dotenv import load_dotenv

# Загрузка .env
load_dotenv()

# Alembic config
config = context.config

# Логгирование
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Здесь будет Base.metadata от твоих моделей
# <-- обязательно импортируем свои модели !!!
from app.models.base import Base
from app.models.author import Author
from app.models.book import Book
from app.models.user import User
from app.models.order import Order
target_metadata = Base.metadata

# Чтение URL из .env (можно и напрямую из config.get_main_option("sqlalchemy.url"))
DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(DATABASE_URL, echo=True)

    async with connectable.connect() as connection:
        def do_run_migrations(connection_):
            context.configure(
                connection=connection_,
                target_metadata=target_metadata,
                compare_type=True,
            )
            with context.begin_transaction():
                context.run_migrations()

        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())

from sqlalchemy.ext.asyncio import create_async_engine

from db.config import settings

engine = create_async_engine(
    url=settings.db_url_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,

)


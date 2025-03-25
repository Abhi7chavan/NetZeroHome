from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL_SYNC = "postgresql://postgres:admin@localhost/smarthome"  # Uses psycopg2
DATABASE_URL_ASYNC = "postgresql+asyncpg://postgres:admin@localhost/smarthome"  # Uses asyncpg

# Sync Engine & Session
sync_engine = create_engine(DATABASE_URL_SYNC)
SyncSessionLocal = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False, expire_on_commit=False)

# Async Engine & Session
async_engine = create_async_engine(DATABASE_URL_ASYNC)
AsyncSessionLocal = sessionmaker(bind=async_engine, expire_on_commit=False)

# Function to get Sync DB Session
def get_db():
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to get Async DB Session
async def get_async_db():
    async with AsyncSessionLocal() as db:
        yield db


Base  = declarative_base()

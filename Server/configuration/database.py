from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser
import os


config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), "configuration/config.ini"))

url = f"postgresql+asyncpg://postgres:admin@localhost:5432/smarthome"
engine = create_async_engine(url,pool_size=20,max_overflow=5,pool_timeout=30,pool_recycle=1800)  # pool_size - maintain 10 open connection for resue and pool_recycle for closes idle connections for 30 min avoid stale connection.
async_db = sessionmaker(bind=engine)
Base  = declarative_base()

async def get_db():
    async with async_db() as session:
        yield session
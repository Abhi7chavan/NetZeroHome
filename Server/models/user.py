from sqlalchemy import Integer,String,Column,func ,ARRAY ,DateTime
import uuid
from Server.configuration.database import Base

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'meta'} 
    user_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    password = Column(String)
    location = Column(String)
    features = Column(ARRAY(String))
    household_items = Column(ARRAY(String))
    sensor_count = Column(ARRAY(String))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
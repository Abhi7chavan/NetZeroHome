from sqlalchemy import String,Column,func,Integer ,ARRAY ,DateTime
import uuid
from configuration.database import Base

class Users(Base):
    __tablename__ = "User"
    __table_args__ = {'schema': 'meta'} 
    user_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    license_id = Column(String,unique=True)
    username = Column(String,unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    location = Column(String)
    features = Column(ARRAY(String))
    HouseholdItems = Column(ARRAY(String))
    SensorCount = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
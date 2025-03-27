from sqlalchemy import String,Column,BigInteger,Integer ,ARRAY ,text 
import time
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
    role_id = Column(String,ForeignKey="role.role_id") #default role id Admin
    created_at = Column(BigInteger, default=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))
    updated_at = Column(BigInteger, default=lambda: int(time.time()), onupdate=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))
    
    
class UserSchema:
    license_id:str
    username:str
    email:str
    password:str
    location:str
    features:str
    HouseholdItems:ARRAY
    SensorCount:ARRAY
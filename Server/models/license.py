from pydantic import BaseModel
from configuration.database import Base
from sqlalchemy import Column,Integer,String,ARRAY
import uuid
class License(Base):
    __tablename__ = "License"
    __table_args__ = {'schema': "meta"} 
    
    license_id = Column(String,default=lambda:str(uuid.uuid4()),primary_key=True)
    name = Column(String)
    lastname = Column(String)
    username = Column(String,unique=True)
    password = Column(String)
    email = Column(String)
    location = Column(String)
    features = Column(ARRAY(String))
    HouseholdItems = Column(ARRAY(String))
    SensorCount = Column(Integer)
     
    
class licenseschema(BaseModel):
    name:str
    lastname:str
    username:str
    password:str
    email:str
    location:str
    features:list
    HouseholdItems:list
    SensorCount:int
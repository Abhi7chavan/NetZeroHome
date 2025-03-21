from Server.configuration.database import Base
from sqlalchemy import Column,Integer,String,ARRAY
import uuid
class License(Base):
    __tablename__ = 'license'
    __table_args__ = {'schema': 'meta'} 
    
    license_id = Column(String,default=lambda:str(uuid.uuid4()),primary_key=True)
    name = Column(String)
    username = Column(String,Foreignkey=('users.username'),unique=True)
    email = Column(String)
    lastname = Column(String)
    location = Column(String)
    features = Column(ARRAY(String))
    household_items = Column(ARRAY(String))
    sensor_count = Column(Integer)
    
    
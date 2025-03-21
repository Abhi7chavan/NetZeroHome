import uuid
from sqlalchemy import Column, String, JSON, Boolean, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class House(Base):
    __tablename__ = 'house'
    __table_args__ = {'schema': 'meta'} 
    
    house_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, nullable=False)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    rooms = Column(JSON, nullable=False)
    location = Column(String)
    issolar = Column(Boolean, nullable=False)
    electric_vehicles = Column(Integer)
    number_of_devices = Column(Integer)

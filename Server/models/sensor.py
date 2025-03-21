import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'meta'} 
    sensor_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)

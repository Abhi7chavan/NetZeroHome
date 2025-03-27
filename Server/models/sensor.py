import uuid
from sqlalchemy import Column, String, ForeignKey,BigInteger,text
import time
from sqlalchemy.ext.declarative import declarative_base
from configuration.database import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'meta'} 
    sensor_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(BigInteger, default=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))
    updated_at = Column(BigInteger, default=lambda: int(time.time()), onupdate=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))

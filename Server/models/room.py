import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    __table_args__ = {'schema': 'meta'} 
    room_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, nullable=False)
    house_id = Column(String, ForeignKey('house.house_id'), nullable=False)

import uuid
from sqlalchemy import Column, String, Float, Numeric, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from configuration.database import Base

class HouseRoomItemMapping(Base):
    __tablename__ = 'house_room_item_mapping'
    __table_args__ = {'schema': 'meta'} 
    
    mapping_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, nullable=False)
    house_id = Column(String, ForeignKey('house.house_id'), nullable=False)
    room_id = Column(String, ForeignKey('room.room_id'), nullable=False)
    sensor_id = Column(String, ForeignKey('sensor.sensor_id'), nullable=False)
    item_id = Column(String, ForeignKey('house_item.item_id'), nullable=False)

class HouseReading(Base):
    __tablename__ = 'house_reading'
    
    # Note: if there are multiple readings per user, you might want to include a primary key column.
    # Here, I'm assuming that each reading is uniquely identified by the combination of user_id and time.
    # Alternatively, you can add an auto-generated primary key.
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    total_energy = Column(Float, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    time = Column(DateTime)

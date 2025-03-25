from configuration.database import Base
from sqlalchemy import Column,Float,String,ARRAY
import uuid


class HouseItem(Base):
    __tablename__ = 'house_item'
    __table_args__ = {'schema': 'meta'} 
    
    item_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    item_name = Column(String, nullable=False)
    voltage_volts = Column(Float, nullable=False)
    current_amps = Column(Float)
    power_watts = Column(Float)
    operating_time_hours = Column(Float)
    power_factor = Column(Float)
    min_power_watts = Column(Float)
    max_power_watts = Column(Float)
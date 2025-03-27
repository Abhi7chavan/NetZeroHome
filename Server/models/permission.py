from configuration.database import Base
import time
from sqlalchemy import Column,String,ARRAY ,ForeignKey,JSON,BigInteger,text
import uuid

class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = {'schema': 'meta'} 
    permission_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    config = Column(JSON)
    created_at = Column(BigInteger, default=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))
    updated_at = Column(BigInteger, default=lambda: int(time.time()), onupdate=lambda: int(time.time()), server_default=text("EXTRACT(EPOCH FROM now())"))

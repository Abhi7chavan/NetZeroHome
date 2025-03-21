from Server.configuration.database import Base
from sqlalchemy import Column,String,ARRAY ,ForeignKey,JSON,DateTime,func
import uuid

class Permission(Base):
    __tablename__ = 'permission'
    __table_args__ = {'schema': 'meta'} 
    permission_id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    config = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

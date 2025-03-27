from configuration.database import Base
from sqlalchemy import Column,String,Text,JSON
import uuid

class role(Base):
    __tablename__ = 'role'
    __table_args__ = {'schema':'meta'}
    
    role_id = Column(String ,default=lambda str:(uuid.uuid4()),primary_key=True,nullable=False)
    name = Column(String,unique=True,nullable=False)
    permission = Column(JSON,nullale=False)
    description = Column(Text)
    
    
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
import uuid
from sqlalchemy import Column, String, JSON, Boolean, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from configuration.database import Base



class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'schema':'meta'}
    category_id = Column(String,default=lambda:str(uuid.uuid4()),primary_key=True,nullable=False)
    name = Column(String,nullable =False)
from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class StateModel(Base):
  __tablename__ = "states"
  id = Column(Integer, primary_key=True, index=True)
  status = Column(String)
  
  books = relationship("BookModel", back_populates="status")
  
  
  
  
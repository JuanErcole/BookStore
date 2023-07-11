from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class BookModel(Base):
  __tablename__ = "books"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255))
  description = Column(String(255))  
  owner_id = Column(Integer, ForeignKey('users.id'))  
  status_id = Column(Integer, ForeignKey('states.id'))

  user = relationship("UserModel", back_populates="books")
  status = relationship("StateModel", back_populates="books")




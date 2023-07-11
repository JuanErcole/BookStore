from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.sql.schema import ForeignKey
from models.country import CountryModel

class UserModel(Base):
  
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)
  role = Column(String)
  country_id = Column(Integer, ForeignKey('country.country_id'))
  
  country = relationship("CountryModel", back_populates="user")
  books = relationship("BookModel", back_populates="user")








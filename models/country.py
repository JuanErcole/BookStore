from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class CountryModel(Base):
  __tablename__ = "country"
  country_id = Column(Integer, primary_key=True, index=True)
  country_name = Column(String(255))
  
  user = relationship("UserModel", back_populates="country")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
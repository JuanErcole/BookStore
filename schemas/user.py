from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
  name: str
  email: str
  password: str
  role: str
  country_id: int
  
  
class User(UserCreate):
  id: int
  
  class Config:
    orm_mode = True


  










from pydantic import BaseModel

class BookCreate(BaseModel):
  name: str
  description: str
  owner_id: int
  status_id: int

class Book(BookCreate):
  id: int

  class Config:
    orm_mode = True



from pydantic import BaseModel

class StateCreate(BaseModel):
  status: str

class State(StateCreate):
  id: int
  class Config:
    orm_mode = True
from pydantic import BaseModel

class CountryCreate(BaseModel):
  country_name: str

class Country(CountryCreate):
  country_id: int
  class Config:
    orm_mode = True

        
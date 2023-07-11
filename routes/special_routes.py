from db import db_dependency
from fastapi import APIRouter

from services.special_services import get_books_by_user, get_users_by_country

router_special = APIRouter(prefix='/special', tags=['Special'])

@router_special.get("/")
def get_special_users( db: db_dependency, country_id: int ):
  return get_users_by_country(db, country_id)

@router_special.get("/get_books_by_owner/{owner_id}")
def get_all_books_by_owner(owner_id: int, db: db_dependency):
  return get_books_by_user(db, owner_id)








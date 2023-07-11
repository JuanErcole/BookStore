from fastapi_crudrouter import SQLAlchemyCRUDRouter
from schemas.country import Country, CountryCreate
from models.country import CountryModel
from db import get_db

router_country = SQLAlchemyCRUDRouter(
  schema= Country,
  create_schema= CountryCreate,
  db_model= CountryModel,
  db=get_db,
  delete_all_route=False,
  update_route=False,
  prefix="/country"
)
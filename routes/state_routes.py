from fastapi_crudrouter import SQLAlchemyCRUDRouter
from schemas.state import State, StateCreate
from models.state import StateModel
from db import get_db

router_state = SQLAlchemyCRUDRouter(
  schema= State,
  create_schema= StateCreate,
  db_model= StateModel,
  db=get_db,
  delete_all_route=False,
  prefix="/state"
)
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from schemas.book import Book, BookCreate
from models.book import BookModel
from db import get_db

router_book = SQLAlchemyCRUDRouter(
  schema= Book,
  create_schema= BookCreate,
  db_model= BookModel,
  db=get_db,
  delete_all_route=False,
  prefix="/book"
)
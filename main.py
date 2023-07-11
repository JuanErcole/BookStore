from fastapi import FastAPI
from db import create_tables
from routes.user_route import router_user
from routes.special_routes import router_special
from routes.country_routes import router_country
from routes.book_routes import router_book
from routes.state_routes import router_state

app = FastAPI()

create_tables()

@app.get("/")
def read_root():
  return 'Holiss'

app.include_router(router_user, tags=['Users'])
app.include_router(router_country, tags=['Country'])
app.include_router(router_book, tags=['Book'])  
app.include_router(router_state, tags=['State'])
app.include_router(router_special)












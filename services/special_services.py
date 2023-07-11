from fastapi import HTTPException
from models.country import CountryModel
from models.user import UserModel


def get_users_by_country(db, country_id):
  country = db.query(CountryModel).filter_by(country_id= country_id).first()
  if not country:
    raise HTTPException(status_code=404, detail="El pais ingresado no es correcto o ya no se encuentra disponible")
  users = country.user
  user_names = [user.name for user in users]
  response = f'En {country.country_name} hay {len(users)} usuarios, los cuales son: {", ".join(user_names)}' 
  if users == []:
    response = f'En {country.country_name} no hay usuarios'
  return response
  

def get_books_by_user(db, owner_id):
  
  user = db.query(UserModel).filter_by(id= owner_id).first()
  
  if not user:
    raise HTTPException(status_code=404, detail="El usuario ingresado no es correcto o ya no se encuentra disponible")
  
  books = user.books
  if books == []:
    return f'{user.name} no tiene libros'
  
  book_names = [book.name for book in books]
  
  book_not_available = [book.status_id for book in books if book.status_id == 2]
  response = f'{user.name} tiene {len(books)} libro/s, los cuales son: {", ".join(book_names)}. {len(book_not_available)} estan prestados' 
  
  if book_not_available == []:
    response = f'{user.name} tiene {len(books)} libro/s: los cuales son: {", ".join(book_names)}.'
  
  
  return response
      



















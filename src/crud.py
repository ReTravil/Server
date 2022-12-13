from sqlalchemy.orm import Session

from src import models, schemas


def create_book(db: Session, book: schemas.BookCreate):

    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book




def create_reader(db: Session, reader: schemas.ReaderCreate):

    db_reader = models.Reader(**reader.dict())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader

def create_theme(db: Session, theme: schemas.ThemeCreate):

    db_theme = models.Theme(**theme.dict())
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme

def create_reader_book(db: Session, reader_book: schemas.Reader_Book, book_id: int, reader_id: int):

    db_reader_book = models.Reader_Book(**reader_book.dict(), book_id = book_id, reader_id = reader_id)
    db.add(db_reader_book)
    db.commit()
    db.refresh(db_reader_book)
    return db_reader_book



def create_instance(db: Session, instance: schemas.InstanceCreate, book_id: int, theme_id: int ):

    db_instance = models.Instance(**instance.dict(), theme_id=theme_id, book_id=book_id)
    # print(db_instance)
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance

def get_book_by_id (db: Session, book_id: int):
    
    return db.query(models.Book).filter(models.Book.id ==book_id).first()

def get_reader_by_id (db: Session, reader_id: int):
    
    return db.query(models.Reader).filter(models.Reader.id ==reader_id).first()

def get_theme_by_id (db: Session, theme_id: int):
    
    return db.query(models.Theme).filter(models.Theme.id ==theme_id).first()

def get_instance_by_id (db: Session, instance_id: int):
    
    return db.query(models.Instance).filter(models.Instance.id == instance_id).first()




def get_book(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Book).offset(skip).limit(limit).all()

def get_reader(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Reader).offset(skip).limit(limit).all()

def get_theme(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Theme).offset(skip).limit(limit).all()

def get_instance(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Instance).offset(skip).limit(limit).all()




def get_book_by_name(db: Session, title:str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_theme_by_name(db: Session, Name:str):
    return db.query(models.Theme).filter(models.Theme.Name == Name).first()

# def get_reader_by_name(db: Session, Name:str):
#     return db.query(models.Reader).filter(models.Reader.Name == Name).first()   


def get_reader_book(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Reader_Book).offset(skip).limit(limit).all()

def get_reader_book_by_id (db: Session, reader_book_id: int):
    
    return db.query(models.Reader_Book).filter(models.Reader_Book.id ==reader_book_id).first()





# def get_user(db: Session, user_id: int):
#     """
#     Получить пользователя по его id
#     """
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     """
#     Получить пользователя по его email
#     """
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     """
#     Получить список предметов из БД
#     skip - сколько записей пропустить
#     limit - маскимальное количество записей
#     """
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     """
#     Получить список пользователей из БД
#     skip - сколько записей пропустить
#     limit - маскимальное количество записей
#     """
#     return db.query(models.User).offset(skip).limit(limit).all()
    
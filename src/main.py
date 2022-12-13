from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db(): # pragma: no cover
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/book/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Создание пользователя, если такой email уже есть в БД, то выдается ошибка
    """
    db_book = crud.get_book_by_name(db, title=book.title)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already registered")
    return crud.create_book(db=db, book=book)


@app.get("/book/", response_model=list[schemas.Book])
def read_book(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    book = crud.get_book(db, skip=skip, limit=limit)
    return book


@app.get("/book/{book_id}", response_model=schemas.Book)
def read_book_by_id(book_id: int, db: Session = Depends(get_db)):

    db_book = crud.get_book_by_id(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/reader/", response_model=schemas.Reader)
def create_reader(reader: schemas.ReaderCreate, db: Session = Depends(get_db)):
    return crud.create_reader(db=db, reader=reader)


@app.get("/reader/", response_model=list[schemas.Reader])
def read_reader(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    reader = crud.get_reader(db, skip=skip, limit=limit)
    return reader


@app.get("/reader/{reader_id}", response_model=schemas.Reader)
def read_reader_by_id(reader_id: int, db: Session = Depends(get_db)):

    db_reader = crud.get_reader_by_id(db, reader_id=reader_id)
    if db_reader is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_reader 

@app.post("/theme/", response_model=schemas.Theme)
def create_theme(theme: schemas.ThemeCreate, db: Session = Depends(get_db)):

    db_theme = crud.get_theme_by_name(db, Name=theme.Name)
    if db_theme:
        raise HTTPException(status_code=400, detail="Theme already registered")
    return crud.create_theme(db=db, theme=theme)


@app.get("/theme/", response_model=list[schemas.Theme])
def read_theme(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    theme = crud.get_theme(db, skip=skip, limit=limit)
    return theme


@app.get("/theme/{theme_id}", response_model=schemas.Theme)
def read_theme_by_id(theme_id: int, db: Session = Depends(get_db)):

    db_theme = crud.get_theme_by_id(db, theme_id=theme_id)
    return db_theme 

@app.get("/instance/", response_model=list[schemas.Instance])
def read_instance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    isinstance = crud.get_instance(db, skip=skip, limit=limit)
    return isinstance


@app.get("/instance/{instance_id}", response_model=schemas.Instance)
def read_istance_by_id(instance_id: int, db: Session = Depends(get_db)):

    db_instance = crud.get_instance_by_id(db, instance_id=instance_id)
    return db_instance 


@app.post("/instance/{theme_id}/{book_id}/", response_model=schemas.Instance)
def create_instance(theme_id: int, book_id: int, instance: schemas.InstanceCreate, db: Session = Depends(get_db)):
    return crud.create_instance(db=db, instance = instance, book_id=book_id, theme_id=theme_id)

@app.get("/reader_book/", response_model=list[schemas.Reader_Book])
def read_reader_book(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    reader_book = crud.get_reader_book(db, skip=skip, limit=limit)
    return reader_book

@app.get("/reader_book/{reader_book_id}", response_model=schemas.Reader_Book)
def reader_book_by_id(reader_book_id: int, db: Session = Depends(get_db)):

    db_reader_book = crud.get_reader_book_by_id(db, reader_book_id = reader_book_id)
    return db_reader_book

@app.post("/reader_book/{book_id}/{reader_id}/", response_model=schemas.Reader_Book)
def create_reader_book(book_id: int, reader_id: int, reader_book: schemas.Reader_BookCreate, db: Session = Depends(get_db)):
    return crud.create_reader_book(db=db, reader_book = reader_book, book_id=book_id, reader_id=reader_id)
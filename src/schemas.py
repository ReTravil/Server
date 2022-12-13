from pydantic import BaseModel
from datetime import date

class Reader_BookBase(BaseModel):
    pass

class Reader_BookCreate(Reader_BookBase):
    pass

class Reader_Book(Reader_BookBase):
    id: int
    book_id: int
    reader_id : int

    class Config:
        orm_mode = True


class InstanceBase(BaseModel):
    Books_have: str
    inventory_number: str
    date_giving: date  
    date_comback: date
    code_theme: int


class InstanceCreate(InstanceBase):
    pass


class Instance(InstanceBase):
    id: int
    book_id: int
    theme_id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):

    title: str
    first_author: str
    year: date
    cost: int
    publisher: str 
    publisher_place: str 
    pages: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    instance: list[Instance]=[]
    reader_book: list[Reader_Book]=[]

    class Config:
        orm_mode = True


 
class ReaderBase(BaseModel):
    Name:str
    date_of_birthday:date
    phone_humber:str 

class ReaderCreate(ReaderBase):
    pass


class Reader(ReaderBase):
    id: int
    reader_book: list[Reader_Book]=[]

    class Config:
        orm_mode = True


class ThemeBase(BaseModel):
    Name:str

class ThemeCreate(ThemeBase):
    pass


class Theme(ThemeBase):
    id: int
    instance: list[Instance]=[]

    class Config:
        orm_mode = True





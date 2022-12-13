from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self): # pragma: no cover
        return f"<{type(self).__name__}(id={self.id})>"


class Book(BaseModel):
    __tablename__ = "books"

    title = Column(String, unique=True)
    first_author = Column(String)
    publisher = Column(String)
    publisher_place = Column(String)
    year = Column(DateTime)
    pages = Column(Integer)
    cost = Column(Integer)

    instance = relationship("Instance", back_populates="book")
    reader_book=relationship("Reader_Book", back_populates="book")


class Instance(BaseModel):
    __tablename__ = "instances"

    Books_have = Column(String)
    inventory_number = Column(String)
    date_giving = Column(DateTime)  
    date_comback = Column(DateTime)
    code_theme =Column(Integer) 
    theme_id = Column(Integer, ForeignKey("themes.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    theme = relationship("Theme", back_populates="instance")
    book = relationship("Book", back_populates="instance")


class Reader(BaseModel):
    __tablename__ = "readers"

    Name = Column(String)
    date_of_birthday = Column(DateTime)
    phone_humber = Column(String) 

    reader_book=relationship("Reader_Book", back_populates="reader")

class Theme(BaseModel):
    __tablename__ = "themes"

    Name = Column(String) 

    instance = relationship("Instance", back_populates="theme")

class Reader_Book(BaseModel):
    __tablename__ = "reader_books"
        
    book_id = Column(Integer, ForeignKey("books.id"))
    reader_id = Column(Integer, ForeignKey("readers.id"))

    book = relationship("Book",back_populates= "reader_book") 
    reader = relationship("Reader", back_populates = "reader_book")



"""Init

Revision ID: fa4745bc794b
Revises: 
Create Date: 2022-12-11 19:00:08.876287

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime

from src.models import Reader, Instance, Theme, Book, Reader_Book

# revision identifiers, used by Alembic.
revision = 'first_data_.py'
down_revision = 'fa4745bc794b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind = bind)

    Book_first = Book(title = 'Вокруг света за 80 дней', first_author = 'Жуль Верн', publisher = 'Азбука', publisher_place = 'Курган', year = datetime(2000, 1, 1), pages = '1000', cost = '2000') 
    Book_second = Book(title = '1000 лье под водой', first_author = 'Жуль Верн', publisher = 'Азбука', publisher_place = 'Курган', year = datetime(2000, 1, 1), pages = '1000', cost = '2000') 
    session.add_all([Book_first, Book_second])
    session.flush()

    Reader_first = Reader(Name ='Дмитрий', date_of_birthday =datetime(2002,9,3), phone_humber='4343413249') 
    Reader_second = Reader(Name ='Данил', date_of_birthday = datetime(2002,9,3), phone_humber='4343413249') 
    
    session.add_all([Reader_first, Reader_second ])
    session.flush()

    Theme_first = Theme( Name = 'Приключения')
    session.add_all([Theme_first])
    session.flush()

    Instance_first = Instance(Books_have = '5', inventory_number = '1', date_giving = datetime(2022, 1, 25, 10, 10), date_comback = datetime(2022, 1, 25, 10, 10), code_theme = '1', theme_id = Theme_first.id, book_id=Book_first.id)
    Instance_second = Instance(Books_have = '5', inventory_number = '1', date_giving = datetime(2022, 1, 25, 10, 10), date_comback = datetime(2022, 1, 25, 10, 10), code_theme = '1', theme_id = Theme_first.id, book_id=Book_second.id)
    session.add_all([Instance_first, Instance_second ])
    session.commit()

    Readbook = Reader_Book(book_id=Book_first.id,reader_id = Reader_first.id)
    Readbook2 = Reader_Book(book_id=Book_second.id,reader_id = Reader_second.id)
    session.add_all([Readbook, Readbook2])
    session.commit()

def downgrade() -> None:
    pass

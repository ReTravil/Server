from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date
from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_book():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/book/",
        json={"title": "1984", "first_author": "Оруэл", "year":"2000", "cost":"2000", "publisher":"Азбука", "publisher_place":"Курган", "pages":"200", "id":1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "1984"

def test_create_reader():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/reader/",
        json={"Name": "Дима", "date_of_birthday": "2000", "phone_humber":"89638664896", "id":1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["Name"] == "Дима"

def test_create_theme():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/theme/",
        json={"Name": "Приключения"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["Name"] == "Приключения"

def test_create_theme_1():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/theme/",
        json={"Name": "Приключения"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Theme already registered"

def test_create_reader_book():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/reader_book/1/1/",
        json={"book_id":1, "reader_id":1,'id':1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["book_id"] == 1

def test_create_instance():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/instance/1/1/",
        json={"book_id":1, "theme_id":1,'id':1, "Books_have":'5',"inventory_number":'1','date_giving':str(date.today()),'date_comback':str(date.today()),'code_theme':1})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["book_id"] == 1
 


def test_create_exist_book():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/book/",
        json={"title": "1984", "first_author": "Оруэл", "year":"2000", "cost":"2000", "publisher":"Азбука", "publisher_place":"Курган", "pages":"200" }
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Book already registered"


def test_get_book():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/book/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "1984"

def test_get_reader():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/reader/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["Name"] == "Дима" 

def test_get_reader_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/reader/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["Name"] == "Дима"

def test_get_reader_by_id_1():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/reader/134")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"

def test_get_book_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/book/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "1984"


def test_book_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/book/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Book not found"


def test_get_instance(): 
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/instance/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["Books_have"] == "5" 

def test_get_theme(): 
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/theme/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["Name"] == "Приключения"

def test_get_theme_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/theme/1")
    assert response.status_code == 200, response.text
    data = response.json()
    print(data)
    assert data["Name"] == "Приключения"

def test_get_instance_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/instance/1")
    assert response.status_code == 200, response.text
    data = response.json()
    print(data)
    assert data["Books_have"] == "5"


def test_get_reader_book(): 
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/reader_book/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["id"] == 1

def test_get_reader_book_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/reader_book/1")
    assert response.status_code == 200, response.text
    data = response.json()
    print(data)
    assert data["id"] == 1



# def test_add_item_to_user():
#     """
#     Тест на добавление Item пользователю
#     """
#     response = client.post(
#         "/users/1/items/",
#         json={"title": "SomeBook", "description": "foobar"}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["title"] == "SomeBook"
#     assert data["description"] == "foobar"
#     assert data["owner_id"] == 1


# def test_get_items():
#     """
#     Тест на получение списка Item-ов из БД
#     """
#     response = client.get("/items/")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["title"] == "SomeBook"
#     assert data[0]["description"] == "foobar"
#     assert data[0]["owner_id"] == 1
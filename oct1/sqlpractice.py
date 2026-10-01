from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

# Описание таблицы в виде Python-класса
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]

# Создаем базу данных (SQLite) и таблицы
engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)

# Работа с данными через сессию
with Session(engine) as session:
    # Добавление записи
    new_user = User(name="Charlie", age=28)
    session.add(new_user)
    session.commit()

    # Запрос данных
    users = session.query(User).filter(User.age >= 25).all()
    for u in users:
        print(f"ID: {u.id}, Имя: {u.name}")
"""
Да, ключевые слова вроде INTEGER, REAL, TEXT, PRIMARY KEY, NOT NULL — это ключевые инструкции для базы данных. Они задают типы данных и ограничения (constraints) для каждого столбца.

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary REAL CHECK (salary > 0),
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE SET NULL
)
SQLite очень гибкий (динамический).
При определении столбцов таблицы для них необходимо указать тип данных. Каждый столбец имеет определенный тип данных. Для хранения данных в в SQLite применяются следующие типы:

NULL: указывает фактически на отсутствие значения

INTEGER: представляет целое число, которое может быть положительным и отрицательным и в зависимости от своего значения может занимать 1, 2, 3, 4, 6 или 8 байт

REAL: представляет число с плавающей точкой, занимает 8 байт в памяти

TEXT: строка текста в одинарных кавычках, которая сохраняется в кодировке базы данных (UTF-8, UTF-16BE или UTF-16LE)

BLOB: бинарные данные
    
"""
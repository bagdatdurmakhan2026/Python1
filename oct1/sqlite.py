import sqlite3
# Подключение к файлу базы данных (если файла нет, он создастся)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
# 1. Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
# 2. Вставка данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()
# 3. Чтение данных (SELECT)
cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
rows = cursor.fetchall()
for row in rows:
    print(row)  # (1, 'Alice', 25), (2, 'Bob', 30)
conn.close()
#Библиотека sqlite3 идет из коробки — вам не нужно ничего устанавливать или запускать отдельные сервисы. База данных хранится в одном файле.
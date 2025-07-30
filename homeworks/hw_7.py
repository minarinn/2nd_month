import sqlite3

def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
            CREATE TABLE IF NOT EXISTS books(
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

def insert_books():
    books = [
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 700, 3),
        ("Война и мир", "Лев Толстой", 1869, "Исторический роман", 1250, 2),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 850, 4),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 450, 5),
        ("Отцы и дети", "Иван Тургенев", 1862, "Роман", 300, 3),
        ("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 250, 2),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Роман в стихах", 200, 6),
        ("Идиот", "Фёдор Достоевский", 1869, "Роман", 750, 2),
        ("Обломов", "Иван Гончаров", 1859, "Роман", 550, 4),
        ("Доктор Живаго", "Борис Пастернак", 1957, "Роман", 600, 3)
    ]
    conn.executemany("""
        INSERT INTO books(name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()

def select_books():
    result = conn.execute("SELECT * FROM books")
    for book in result:
        print(book)


if __name__ == "__main__":
    conn = sqlite3.connect("../database.sqlite")
    create_table()
    insert_books()
    select_books()
    conn.close()

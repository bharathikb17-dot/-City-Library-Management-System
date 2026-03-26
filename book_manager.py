from storage import read_data, write_data

BOOK_FILE = "data/books.csv"

def add_book(book_id, title, author, genre):
    df = read_data(BOOK_FILE)

    if not df.empty and book_id in df['book_id'].values:
        return "Book already exists"

    new = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "genre": genre,
        "available": "Yes"
    }

    df = df._append(new, ignore_index=True)
    write_data(BOOK_FILE, df)

    return "Book added successfully"

def get_books():
    return read_data(BOOK_FILE)
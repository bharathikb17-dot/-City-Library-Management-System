from storage import read_data, write_data
import pandas as pd
import os

BOOK_FILE = "data/books.csv"

def generate_book_id():
    if not os.path.exists(BOOKS_FILE):
        return "B001"

    df = pd.read_csv(BOOKS_FILE)

    if df.empty:
        return "B001"

    # Extract numeric part and find max
    df["num"] = df["Book ID"].str.replace("B", "").astype(int)
    next_id = df["num"].max() + 1

    return f"B{str(next_id).zfill(3)}"


def add_book(title, author, genre):
    book_id = generate_book_id()

    new_book = pd.DataFrame([{
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Availability": "Available"
    }])

    if os.path.exists(BOOKS_FILE):
        df = pd.read_csv(BOOKS_FILE)
        df = pd.concat([df, new_book], ignore_index=True)
    else:
        df = new_book

    df.to_csv(BOOKS_FILE, index=False)

    return f"✅ Book added successfully with ID: {book_id}"
def get_books():
    return read_data(BOOK_FILE)
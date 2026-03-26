import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from storage import read_data
from utils import calculate_fine

TRANS_FILE = "data/transactions.csv"
BOOK_FILE = "data/books.csv"

def fine_statistics():
    trans = read_data(TRANS_FILE)

    if trans.empty:
        return "No transactions yet"

    fines = [calculate_fine(row['due_date']) for _, row in trans.iterrows()]
    arr = np.array(fines)

    return {
        "Total Fine": int(np.sum(arr)),
        "Average Fine": float(np.mean(arr)),
        "Max Fine": int(np.max(arr))
    }

def popular_genre_chart():
    trans = read_data(TRANS_FILE)
    books = read_data(BOOK_FILE)

    if trans.empty:
        return None

    merged = pd.merge(trans, books, on="book_id")
    counts = merged['genre'].value_counts()

    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax)
    ax.set_title("Most Popular Genres")

    return fig
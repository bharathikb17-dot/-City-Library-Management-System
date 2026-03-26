from storage import read_data, write_data
from utils import get_due_date, calculate_fine

BOOK_FILE = "data/books.csv"
TRANS_FILE = "data/transactions.csv"

def borrow_book(member_id, book_id):
    books = read_data(BOOK_FILE)
    trans = read_data(TRANS_FILE)

    if book_id not in books['book_id'].values:
        return "Book not found"

    if books.loc[books['book_id'] == book_id, 'available'].values[0] == "No":
        return "Book not available"

    books.loc[books['book_id'] == book_id, 'available'] = "No"

    due_date = get_due_date()

    new = {
        "member_id": member_id,
        "book_id": book_id,
        "due_date": due_date,
        "returned": "No"
    }

    trans = trans._append(new, ignore_index=True)

    write_data(BOOK_FILE, books)
    write_data(TRANS_FILE, trans)

    return f"Book issued successfully. Due date: {due_date}"

def return_book(member_id, book_id):
    books = read_data(BOOK_FILE)
    trans = read_data(TRANS_FILE)

    record = trans[
        (trans['book_id'] == book_id) &
        (trans['member_id'] == member_id) &
        (trans['returned'] == "No")
    ]

    if record.empty:
        return "No transaction found"

    due_date = record.iloc[0]['due_date']
    fine = calculate_fine(due_date)

    trans.loc[record.index, 'returned'] = "Yes"
    books.loc[books['book_id'] == book_id, 'available'] = "Yes"

    write_data(BOOK_FILE, books)
    write_data(TRANS_FILE, trans)

    return f"Book returned. Fine: ₹{fine}"
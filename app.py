import streamlit as st
import pandas as pd
from book_manager import add_book, get_books
from member_manager import add_member
from transaction import borrow_book, return_book
from analytics import fine_statistics, popular_genre_chart

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Library System", layout="wide")

st.title("📚 City Library Management System")

# -------------------------------
# SIDEBAR TITLE (BIGGER & BOLD)
# -------------------------------
st.sidebar.markdown("## 📌 Navigation")

# -------------------------------
# SIDEBAR MENU (WITH HIGHLIGHT)
# -------------------------------
menu = st.sidebar.radio(
    "",
    ["📘 View Books", "📚 Add Book", "👤 Add Member", "📖 Borrow", "🔄 Return", "👥 View Members", "📊 Analytics"]
)

# -------------------------------
# VIEW BOOKS
# -------------------------------
if menu == "📘 View Books":
    st.subheader("📘 Book List")
    st.dataframe(get_books(), use_container_width=True)

# -------------------------------
# ADD BOOK (AUTO ID)
# -------------------------------
elif menu == "📚 Add Book":
    st.subheader("📚 Add Book")

    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")

    if st.button("➕ Add Book"):
        if title and author:
            st.success(add_book(title, author, genre))
        else:
            st.warning("Please fill all required fields")

# -------------------------------
# ADD MEMBER (FIXED INPUT)
# -------------------------------
elif menu == "👤 Add Member":
    st.subheader("👤 Add Member")

    member_id = st.text_input("Member ID")
    name = st.text_input("Name")
    age = st.number_input("Age")
    contact = st.text_input("Contact")

    if st.button("➕ Add Member"):
        st.success(add_member(member_id, name, age, contact))

# -------------------------------
# BORROW BOOK
# -------------------------------
elif menu == "📖 Borrow":
    st.subheader("📖 Borrow Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("📥 Borrow"):
        st.success(borrow_book(member_id, book_id))

# -------------------------------
# RETURN BOOK
# -------------------------------
elif menu == "🔄 Return":
    st.subheader("🔄 Return Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("📤 Return"):
        st.success(return_book(member_id, book_id))

# -------------------------------
# VIEW MEMBERS (NEW)
# -------------------------------
elif menu == "👥 View Members":
    st.subheader("👥 Members List")

    try:
        members_df = pd.read_csv("data/members.csv")
        st.dataframe(members_df, use_container_width=True)
    except:
        st.error("Members file not found")

# -------------------------------
# ANALYTICS
# -------------------------------
elif menu == "📊 Analytics":
    st.subheader("📊 Analytics")

    st.write(fine_statistics())

    fig = popular_genre_chart()
    if fig:
        st.pyplot(fig)

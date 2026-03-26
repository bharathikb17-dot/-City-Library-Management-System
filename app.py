import streamlit as st
from book_manager import add_book, get_books
from member_manager import add_member
from transaction import borrow_book, return_book
from analytics import fine_statistics, popular_genre_chart

st.title("📚 City Library Management System")

menu = st.sidebar.selectbox("Menu",
    ["Add Book", "Add Member", "Borrow", "Return", "View Books", "Analytics"])

if menu == "Add Book":
    st.subheader("Add Book")
    id = st.text_input("Book ID")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")

    if st.button("Add Book"):
        st.success(add_book(id, title, author, genre))

elif menu == "Add Member":
    st.subheader("Add Member")
    if st.button("Add Member"):
        st.success(add_member(
            st.text_input("Member ID"),
            st.text_input("Name"),
            st.number_input("Age"),
            st.text_input("Contact")
        ))

elif menu == "Borrow":
    st.subheader("Borrow Book")
    if st.button("Borrow"):
        st.success(borrow_book(
            st.text_input("Member ID"),
            st.text_input("Book ID")
        ))

elif menu == "Return":
    st.subheader("Return Book")
    if st.button("Return"):
        st.success(return_book(
            st.text_input("Member ID"),
            st.text_input("Book ID")
        ))

elif menu == "View Books":
    st.write(get_books())

elif menu == "Analytics":
    st.subheader("📊 Analytics")
    st.write(fine_statistics())

    fig = popular_genre_chart()
    if fig:
        st.pyplot(fig)
import streamlit as st
import pandas as pd
from book_manager import add_book, get_books
from member_manager import add_member
from transaction import borrow_book, return_book
from analytics import fine_statistics, popular_genre_chart

st.title("📚 City Library Management System")

# -------------------------------
# SESSION STATE FOR MENU
# -------------------------------
if "menu" not in st.session_state:
    st.session_state.menu = "View Books"

# -------------------------------
# BUTTON MENU (REPLACES SELECTBOX)
# -------------------------------
st.markdown("## 📌 Menu")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("📚 Add Book"):
        st.session_state.menu = "Add Book"

with col2:
    if st.button("👤 Add Member"):
        st.session_state.menu = "Add Member"

with col3:
    if st.button("📖 Borrow"):
        st.session_state.menu = "Borrow"

with col4:
    if st.button("🔄 Return"):
        st.session_state.menu = "Return"

with col5:
    if st.button("📘 View Books"):
        st.session_state.menu = "View Books"

with col6:
    if st.button("📊 Analytics"):
        st.session_state.menu = "Analytics"

menu = st.session_state.menu

# -------------------------------
# SIDEBAR - MEMBERS LIST
# -------------------------------
st.sidebar.title("👥 Members List")

try:
    members_df = pd.read_csv("data/members.csv")

    if not members_df.empty:
        search = st.sidebar.text_input("🔍 Search Member")

        if search:
            filtered = members_df[members_df["Name"].str.contains(search, case=False)]
            st.sidebar.dataframe(filtered)
        else:
            st.sidebar.dataframe(members_df)
    else:
        st.sidebar.write("No members available")

except:
    st.sidebar.write("Members file not found")

# -------------------------------
# ADD BOOK
# -------------------------------
if menu == "Add Book":
    st.subheader("Add Book")

    id = st.text_input("Book ID")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")

    if st.button("Add Book"):
        st.success(add_book(id, title, author, genre))

# -------------------------------
# ADD MEMBER (FIXED INPUT ISSUE)
# -------------------------------
elif menu == "Add Member":
    st.subheader("Add Member")

    member_id = st.text_input("Member ID")
    name = st.text_input("Name")
    age = st.number_input("Age")
    contact = st.text_input("Contact")

    if st.button("Add Member"):
        st.success(add_member(member_id, name, age, contact))

# -------------------------------
# BORROW BOOK (FIXED INPUT ISSUE)
# -------------------------------
elif menu == "Borrow":
    st.subheader("Borrow Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Borrow"):
        st.success(borrow_book(member_id, book_id))

# -------------------------------
# RETURN BOOK (FIXED INPUT ISSUE)
# -------------------------------
elif menu == "Return":
    st.subheader("Return Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Return"):
        st.success(return_book(member_id, book_id))

# -------------------------------
# VIEW BOOKS
# -------------------------------
elif menu == "View Books":
    st.subheader("📘 Book List")
    st.write(get_books())

# -------------------------------
# ANALYTICS
# -------------------------------
elif menu == "Analytics":
    st.subheader("📊 Analytics")

    st.write(fine_statistics())

    fig = popular_genre_chart()
    if fig:
        st.pyplot(fig)

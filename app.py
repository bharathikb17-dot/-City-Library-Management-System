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

# -------------------------------
# CUSTOM CSS (PROFESSIONAL UI)
# -------------------------------
st.markdown("""
<style>

/* App background */
.main {
    background-color: #f5f7fa;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    padding: 20px;
}

/* Sidebar menu items */
div[role="radiogroup"] > label {
    padding: 12px;
    margin-bottom: 8px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 15px;
}

/* Active menu */
div[role="radiogroup"] > label[data-checked="true"] {
    background-color: #e0e0e0;
    font-weight: 600;
}

/* Cards */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* Buttons */
div.stButton > button {
    border-radius: 8px;
    padding: 8px 16px;
}

/* Headers */
h1, h2, h3 {
    color: #333;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("📚 City Library Management System")

# -------------------------------
# SIDEBAR MENU
# -------------------------------
menu = st.sidebar.radio(
    "📌 Navigation",
    ["📘 View Books", "📚 Add Book", "👤 Add Member", "📖 Borrow", "🔄 Return", "👥 View Members", "📊 Analytics"]
)

# -------------------------------
# VIEW BOOKS
# -------------------------------
if menu == "📘 View Books":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📘 Book Collection")

    books = get_books()
    st.dataframe(books, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# ADD BOOK
# -------------------------------
elif menu == "📚 Add Book":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📚 Add New Book")

    col1, col2 = st.columns(2)

    with col1:
        book_id = st.text_input("Book ID")
        title = st.text_input("Title")

    with col2:
        author = st.text_input("Author")
        genre = st.text_input("Genre")

    if st.button("➕ Add Book"):
        st.success(add_book(book_id, title, author, genre))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# ADD MEMBER
# -------------------------------
elif menu == "👤 Add Member":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👤 Add Member")

    col1, col2 = st.columns(2)

    with col1:
        member_id = st.text_input("Member ID")
        name = st.text_input("Name")

    with col2:
        age = st.number_input("Age")
        contact = st.text_input("Contact")

    if st.button("➕ Add Member"):
        st.success(add_member(member_id, name, age, contact))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# BORROW BOOK
# -------------------------------
elif menu == "📖 Borrow":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📖 Borrow Book")

    col1, col2 = st.columns(2)

    with col1:
        member_id = st.text_input("Member ID")

    with col2:
        book_id = st.text_input("Book ID")

    if st.button("📥 Borrow"):
        st.success(borrow_book(member_id, book_id))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# RETURN BOOK
# -------------------------------
elif menu == "🔄 Return":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔄 Return Book")

    col1, col2 = st.columns(2)

    with col1:
        member_id = st.text_input("Member ID")

    with col2:
        book_id = st.text_input("Book ID")

    if st.button("📤 Return"):
        st.success(return_book(member_id, book_id))

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# VIEW MEMBERS
# -------------------------------
elif menu == "👥 View Members":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👥 Members")

    try:
        members_df = pd.read_csv("data/members.csv")
        st.dataframe(members_df, use_container_width=True)
    except:
        st.error("Members file not found")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# ANALYTICS
# -------------------------------
elif menu == "📊 Analytics":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Library Analytics")

    st.write(fine_statistics())

    fig = popular_genre_chart()
    if fig:
        st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

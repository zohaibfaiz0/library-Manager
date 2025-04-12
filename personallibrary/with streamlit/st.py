import streamlit as st
import json
import os

FILENAME = "library.json"

# Load and save functions
def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(FILENAME, "w") as f:
        json.dump(library, f)

# Setup session state
if "library" not in st.session_state:
    st.session_state.library = load_library()

st.title("📚 Personal Library Manager")

# Add Book
st.header("➕ Add a Book")
with st.form("add_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", step=1, min_value=0)
    genre = st.text_input("Genre")
    read = st.checkbox("Read?")
    if st.form_submit_button("Add"):
        book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
        st.session_state.library.append(book)
        save_library(st.session_state.library)
        st.success("Book added!")

# Search Book
st.header("🔍 Search Books")
search = st.text_input("Search by title or author")
if search:
    for book in st.session_state.library:
        if search.lower() in book["title"].lower() or search.lower() in book["author"].lower():
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Show All Books
st.header("📖 All Books")
if not st.session_state.library:
    st.info("No books in library.")
else:
    for i, book in enumerate(st.session_state.library):
        status = "✅ Read" if book["read"] else "❌ Unread"
        st.write(f"{i+1}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Remove Book
st.header("❌ Remove a Book")
titles = [book["title"] for book in st.session_state.library]
if titles:
    to_remove = st.selectbox("Select book to remove", titles)
    if st.button("Remove Book"):
        st.session_state.library = [b for b in st.session_state.library if b["title"] != to_remove]
        save_library(st.session_state.library)
        st.success("Book removed!")

# Stats
st.header("📊 Statistics")
total = len(st.session_state.library)
read = sum(b["read"] for b in st.session_state.library)
percent = (read / total * 100) if total > 0 else 0
st.write(f"Total books: {total}")
st.write(f"Books read: {read}")
st.write(f"Percentage read: {percent:.1f}%")

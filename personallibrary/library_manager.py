import os 
import json

FILENAME = "library.txt"

def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(FILENAME, "w") as file:
        json.dump(library, file)

def add_book(library):
   title = input("Enter the book title: ")
   author = input("Enter the author: ")
   year = int(input("Enter the publication year: "))
   genre = input("Enter the genre: ")
   read = input("Have you read this book? (yes/no): ").lower() == "yes"

   book = {
       "title": title,
       "author": author,
       "year": year,
       "genre": genre,
       "read": read,
   }
   library.append(book)
   print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book Not Found!\n")

def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    term = input("Enter the search term: ").lower()

    results = []
    for book in library:
        if choice == "1" and term in book["title"].lower():
            results.append(book)
        elif choice == "2" and term in book["author"].lower():
            results.append(book)
        
    if results:
        print("Matching Books:")
        for i, b in enumerate(results, 1):
            status = "Read" if b["read"] else "Unread"
            print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
    else:
        print("No matching books found.")
    print()

def display_books(library):
    if not library:
        print("No books in the library.\n")
        return
    print("Your Library:")
    for i , b in enumerate(library, 1):
        status = "Read" if b["read"] else "Unread"
        print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
    print()

def display_stats(library):
    total = len(library)
    read_books = sum(1 for b in library if b["read"])
    percent = (read_books / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.1f}%\n")

def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
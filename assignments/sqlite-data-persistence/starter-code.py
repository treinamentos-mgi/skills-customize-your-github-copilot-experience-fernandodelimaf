import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("books.db")


def initialize_database() -> None:
    """Create the books table if it does not already exist."""
    # TODO: Connect to DATABASE_PATH and create the books table.
    pass


def add_book(title: str, author: str) -> int:
    """Add a book and return its database ID."""
    # TODO: Insert the book using a parameterized SQL query.
    pass


def list_books() -> list[tuple[int, str, str]]:
    """Return all books ordered by ID."""
    # TODO: Select and return each book's ID, title, and author.
    pass


def update_book(book_id: int, title: str, author: str) -> bool:
    """Update a book and return whether a matching ID was found."""
    # TODO: Update the matching book and check whether a row was changed.
    pass


def delete_book(book_id: int) -> bool:
    """Delete a book and return whether a matching ID was found."""
    # TODO: Delete the matching book and check whether a row was removed.
    pass


def main() -> None:
    initialize_database()
    print("Books in the catalog:")
    for book in list_books():
        print(book)


if __name__ == "__main__":
    main()

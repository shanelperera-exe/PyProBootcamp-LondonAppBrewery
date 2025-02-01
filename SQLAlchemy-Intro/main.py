from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

## CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Create the extension
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Initialise the app with the extension
db.init_app(app)

## CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
# with app.app_context():
#     # Note: When creating new records, the primary key fields is optional. you can also write
#     # new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)  // the id field will be auto-generated.
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

def create_a_record():
    print("*** Add a new Book ***")
    title = input("Title: ").title().strip()
    author = input("Author: ").title().strip()

    while True:
        try:
            rating = float(input("Rating (Out of 10): "))
            if 0 <= rating <= 10:  # Ensure that the rating is within a valid range
                break
            else:
                print("Please provide a rating between 0 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value for the rating.")
            continue

    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        print("New book has been added successfully!")

def read_all_records():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()

def read_particular_record():
    # By Query
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

def update_record():
    # By Query
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit()

    # By Primary key
    # book_id = 1
    # with app.app_context():
    #     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    #     # or book_to_update = db.get_or_404(Book, book_id)
    #     book_to_update.title = "Harry Potter and the Goblet of Fire"
    #     db.session.commit()

def delete_record():
    # By Primary Key
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()

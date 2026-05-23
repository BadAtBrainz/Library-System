
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

books = [
{
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "year": 2001,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/7884866-L.jpg"
    },{
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/7222246-L.jpg"
    },{
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/7352161-L.jpg"
    },{
        "id": 4,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/6979861-L.jpg"
    },{
        "id": 5,
        "title": "Atomic Habits",
        "author": "James Clear",
        "year": 2018,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/10521270-L.jpg"
    },{
        "id": 6,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "year": 1997,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/240726-L.jpg"
    },{
        "id": 7,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/8101356-L.jpg"
    },{
        "id": 8,
        "title": "Think and Grow Rich",
        "author": "Napoleon Hill",
        "year": 1937,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/8231856-L.jpg"
    },{
        "id": 9,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/9610921-L.jpg"
    },{
        "id": 10,
        "title": "Deep Work",
        "author": "Cal Newport",
        "year": 2016,
        "status": "Available",
        "cover": "https://covers.openlibrary.org/b/id/9259251-L.jpg"
    }
]

members = [
    {"name": "Somchai Jaidee", "email": "somchai1@gmail.com"},
    {"name": "Suda Meechai", "email": "suda2@gmail.com"},
    {"name": "Anan Sukjai", "email": "anan3@gmail.com"},
    {"name": "Malee Thongdee", "email": "malee4@gmail.com"},
    {"name": "Niran Kla", "email": "niran5@gmail.com"},
    {"name": "Kanya Yim", "email": "kanya6@gmail.com"},
    {"name": "Preecha Dee", "email": "preecha7@gmail.com"},
    {"name": "Ladda Suk", "email": "ladda8@gmail.com"},
    {"name": "Chaiwat Thong", "email": "chaiwat9@gmail.com"},
    {"name": "Nok Rakdee", "email": "nok10@gmail.com"},
]

borrow_history = []

@app.route('/')
def home():
    total_books = len(books)
    borrowed_books = len([b for b in books if b["status"] == "Borrowed"])
    available_books = total_books - borrowed_books

    return render_template(
        'index.html',
        books=books,
        total_books=total_books,
        borrowed_books=borrowed_books,
        available_books=available_books
    )

@app.route('/books')
def books_page():
    return render_template('books.html', books=books)

@app.route('/members')
def members_page():
    return render_template('members.html', members=members)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    if request.method == 'POST':
        book_name = request.form.get('book')
        member_name = request.form.get('member')

        for book in books:
            if book["title"] == book_name and book["status"] == "Available":
                book["status"] = "Borrowed"

                borrow_history.append({
                    "book": book_name,
                    "member": member_name,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "status": "Borrowed"
                })

        return redirect(url_for('borrow'))

    return render_template(
        'borrow.html',
        books=books,
        members=members,
        history=borrow_history
    )

@app.route('/return/<book_title>')
def return_book(book_title):

    for book in books:
        if book["title"] == book_title:
            book["status"] = "Available"

    for item in borrow_history:
        if item["book"] == book_title and item["status"] == "Borrowed":
            item["status"] = "Returned"

    return redirect(url_for('borrow'))

if __name__ == '__main__':
    app.run(debug=True)

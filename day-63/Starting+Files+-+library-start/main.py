from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    print(books)
    return render_template('index.html', books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        new_rate = request.form['rating']
        book.rating = new_rate
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('edit.html', book=book)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    book_id = request.args.get('id')
    book = db.get_or_404(Book, book_id)
    if request.method == "GET":
        db.session.delete(book)
        db.session.commit()
        books = db.session.execute(
            db.select(Book).order_by(Book.title)).scalars()
        return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)

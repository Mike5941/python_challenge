from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request
from form import *
from movie_data import *
from pprint import pprint
import request_api

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movie-collections.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@ app.route("/find", methods=["GET", "POST"])
def find():
    movie_id = request.args.get('id')
    if movie_id:
        movie_data = request_api.get_details(movie_id)
        add_new_movie(movie_data)
        return redirect(url_for("home"))


@ app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movie_title = request.form['title']
        result = request_api.search_movie(movie_title)
        return render_template('select.html', movies=result)
    return render_template("add.html", form=add_form)


@ app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    delete_movie(movie_id)
    return redirect(url_for('home'))


@ app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get('id')
    movie = get_movie_data(movie_id)
    rate_form = RateMovieForm()
    if rate_form.validate_on_submit():
        new_rate = request.form['rating']
        new_review = request.form['review']
        edit_movie_data(movie=movie, rate=new_rate, review=new_review)
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=rate_form)


@ app.route("/select", methods=["GET", "POST"])
def select():
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)

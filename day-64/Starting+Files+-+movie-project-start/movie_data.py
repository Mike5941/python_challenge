from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
MOVIE_URL = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


def get_movie_data(id):
    return db.get_or_404(Movie, id)


def add_new_movie(movie_data):
    title = movie_data['title']
    img_url = f"{MOVIE_URL}{movie_data['poster_path']}"
    release_date = movie_data['release_date'].split("-")[0]
    description = movie_data['overview']
    new_movie = Movie(
        title=title,
        year=release_date,
        description=description,
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.commit()


def edit_movie_data(movie, rate, review):
    movie.rating = rate
    movie.review = review
    db.session.commit()


def delete_movie(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()

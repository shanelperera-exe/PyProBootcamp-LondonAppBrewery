from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
from os import environ

load_dotenv()

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = environ["MOVIE_DB_API_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TopMovies.db"
db.init_app(app)

# CREATE DB
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(400), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(300), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

# CREATE TABLE
with app.app_context():
    db.create_all()
@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return  redirect(url_for('home'))

def search_movie(movie_title):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {MOVIE_DB_API_KEY}"
    }
    params = {
        "api_key": MOVIE_DB_API_KEY,
        "query": movie_title,
        "language": "en-US",
        "include_adult": "true",
        "page": 1
    }
    response = requests.get(url=MOVIE_DB_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["results"]

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        data = search_movie(movie_title)
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find", methods=["GET", "POST"])
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_data_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        # The language parameter is optional, if you were making the website for a different audience
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_API_KEY}"
        }
        params = {
            "api_key": MOVIE_DB_API_KEY,
            "language": "en-US"
        }
        response = requests.get(movie_data_api_url, params=params, headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['backdrop_path']}",
            year=int(data["release_date"].split("-")[0]),
            description=data["overview"],
            rating=0,  # Default value
            ranking=0,  # Default value
            review=""  # Default value
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)

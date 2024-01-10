from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = StringField(
        label="Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField()


class AddMovieForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    submit = SubmitField()

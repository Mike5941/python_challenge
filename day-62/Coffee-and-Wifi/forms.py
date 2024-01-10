from wtforms import StringField, URLField, SelectField, SubmitField, TimeField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    location = URLField(label='URL', validators=[DataRequired()])
    opening_time = StringField(validators=[DataRequired()])
    closing_time = StringField(validators=[DataRequired()])
    coffee_rating = SelectField(
        choices=[("☕️"), ("☕️☕️"), ("☕️☕️☕️"), ("☕️☕️☕️☕️"), ("☕️☕️☕️☕️☕️")]
    )
    wifi_strength = SelectField(
        choices=[("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪")]
    )
    power_availability = SelectField(
        choices=[("✘"), ("✘✘"), ("✘✘✘"), ("✘✘✘✘"), ("✘✘✘✘✘")]
    )
    submit = SubmitField()

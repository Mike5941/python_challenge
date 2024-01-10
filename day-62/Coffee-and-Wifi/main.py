from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import CafeForm
import cafe_data


app = Flask(__name__)
app.config['SECRET_KEY'] = "asfasfawe"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cafes", methods=["GET", "POST"])
def cafe():
    return render_template('cafes.html', cafe_graph=cafe_data.update_list())


@app.route("/add", methods=["GET", "POST"])
def add():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        cafe_data.add_newline(cafe_form)
        return render_template('cafes.html', cafe_graph=cafe_data.update_list())
    else:
        return render_template('add.html', form=cafe_form)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "asfasfawe"
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = "mike9159@naver.com"
        password = "12341234"
        if login_form.email.data == email and login_form.password.data == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

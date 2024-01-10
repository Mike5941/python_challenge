import time

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        result = f"<b>{text}</b>"
        return result
    return wrapper

def make_empahsis(function):
    def wrapper():
        text = function()
        result = f"<em>{text}</em>"
        return result
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 css="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/LMn7PRCVDcnvO/giphy.gif" width=200>'


@app.route('/bye')
@make_bold
@make_empahsis
def bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello thee {name}?, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)

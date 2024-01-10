import requests
from flask import Flask
from flask import render_template


app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()

@app.route("/")
def get_home():
    return render_template("base.html", all_posts=posts)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", posts=posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)
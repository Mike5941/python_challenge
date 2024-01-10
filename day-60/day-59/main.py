import requests
import smtplib
from flask import Flask, render_template, request


app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = response.json()

SMTP_EMAIL = "enjoy5941@gmail.com"
SMTP_PASSWORD = "pmrskqsxxirmgokq"

@app.route("/")
def get_home():
    return render_template("base.html", all_posts=posts)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['text']

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=SMTP_EMAIL, password=SMTP_PASSWORD)
            connection.sendmail(
                from_addr=SMTP_EMAIL,
                to_addrs=email,
                msg=f"{name} {phone} {message}"
            )
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)





@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", posts=posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)
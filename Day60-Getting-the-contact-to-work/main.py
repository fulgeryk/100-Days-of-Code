from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method =="POST":
        my_email = "fulger.sorin@yahoo.com"
        password = os.environ.get("password_yahoo")
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        new_list = [name, email, phone, message]
        for n in new_list:
            print(n)
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()  # securizeaza conexiunea
            connection.login(user=my_email, password=password)
            msg = (f"From: {my_email}\nTo: {my_email}\nSubject: New messages from {name}\n\n"
                   f"Name: {name}\n\n"
                   f"Email: {email}\n\n"
                   f"Phone: {phone}\n\n"
                   f"Message: {message}")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=msg
            )
        return render_template("contact.html", metoda=request.method)
    else:
        return render_template("contact.html", metoda=request.method)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

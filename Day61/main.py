from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
load_dotenv()


class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators = [Email(message=("Invalid email address."))])
    password = PasswordField(label = 'Password', validators= [Length(min = 8, message=('Field must be at least 8 characters long.'))])
    submit = SubmitField(label = "Log In")

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = os.environ.get("Secret")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import random

app = Flask(__name__)

def make_heading(function):
    def wrapper():
        return f"<h1><b>{function()}</b></h1>"
    return wrapper

def too_low_decorator(function):
    def wrapper():
        return (f'<h1 style="color: red;">{function()}</h1>'
                f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    return wrapper

def too_high_decorator(function):
    def wrapper():
        return (f'<h1 style="color: blue;">{function()}</h1>'
                f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    return wrapper

def you_got_me_decorator(function):
    def wrapper():
        return (f'<h1 style="color: green;">{function()}</h1>'
                f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    return wrapper

number_need_to_guess = random.randint(0,9)

@app.route("/")
@make_heading
def guess_a_number():
    return ('Guess a number between 0 and 9 <br>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width = 200>')

@too_low_decorator
def too_low():
    return "Too low, try again!"

@too_high_decorator
def too_high():
    return "Too high, try again!"

@you_got_me_decorator
def you_got_me():
    return "You got me!"

@app.route("/<int:number>")
def check_number(number):
    if number < number_need_to_guess:
        return too_low()
    elif number >number_need_to_guess:
        return too_high()
    else:
        return you_got_me()


if __name__ == "__main__":
    app.run(debug=True)
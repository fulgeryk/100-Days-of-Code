from flask import Flask

app = Flask(__name__)

#Randering HTML Elements with Flask
@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!'
            '</h1><p>This a paragraph</p>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWZiMnoxd245cmtzbWRlbjhuZWtpNG1zYmw5aWs1dWNqM2V3c2s0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WZZ2EUCJdl2g9JKYD8/giphy.gif" width=200>')

def make_bold(function):
    def wrapper_function():
       return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old !"

if __name__ == "__main__":
    app.run(debug=True)
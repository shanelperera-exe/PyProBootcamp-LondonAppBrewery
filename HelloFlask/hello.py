from flask import Flask

def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        result = function()
        return  f"<em>{result}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        result = function()
        return  f"<u>{result}</u>"
    return wrapper
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>We have come here in peace.✌️☮️</p>" \
            "<img src=https://external-preview.redd.it/some-of-the-alien-videos-captured-on-ring-doorbell-cams-v0-ZrBFAmfbR4mf9mde9eaIMpZR5C-bj4ajKCQVSjqWzCo.jpg?width=1080&crop=smart&auto=webp&s=96e6b6132209838a743e14aaa0e3f80baea146c8>"

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "bye"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

@app.route("/info")
def alien_info():
    return "<img src=https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/273deb8d-86f8-4fb5-af9e-ee322a81c145/d8epvdb-d7fcb3f8-369a-4e88-b211-b3b17f87710d.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3M2RlYjhkLTg2ZjgtNGZiNS1hZjllLWVlMzIyYTgxYzE0NVwvZDhlcHZkYi1kN2ZjYjNmOC0zNjlhLTRlODgtYjIxMS1iM2IxN2Y4NzcxMGQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.cNJGvflxMQlLrNNP7rogIXHlp4IVZfJcI29e4wGhQ4Q>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
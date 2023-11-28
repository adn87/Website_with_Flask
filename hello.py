from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/1wnZSnmrnwJmnJkd1c/giphy-downsized-large.gif" width=200px>')


# Different routes using the app.route decorator.
@app.route("/bye")
def bye():
    return "Bye"


# Creating variable paths and converting the path to a specified data type.
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! You are {number} years old"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

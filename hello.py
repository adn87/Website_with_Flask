from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)

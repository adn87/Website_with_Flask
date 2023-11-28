# from flask import Flask
import time
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "Hello, World!"
#
#
# if __name__ == "__main__":
#     app.run()


# Creating a python decorator function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_bye():
    print("bye")


def say_greeting():
    print("how are you?")


# this will delay 2 seconds
say_hello()
# this will be triggered right away
say_greeting()
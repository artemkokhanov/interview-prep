# Variable and Keyword arguments example
def arguments_example(*args, **kwargs):
    print(f"Variable arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    print(args[0] + args[1])
    print(kwargs['a'] + kwargs['b'])

# arguments_example(1, 2, 3, a=4, b=5)


# Decorator function:
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned result {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 4)

########################################################################################################################

# Generator function:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

########################################################################################################################

# OOP Example:
# Main OOP concepts:
# Classes and Objects
# Encapsulation (using private vars and accessing them using getter methods for example)
# Inheritance
# Polymorphism
# Abstraction (generalized method to be implemented for specific classes that will inherit class of generalized method for example)
# Composition (composing a Class of multiple different other classes for example)

class Library:
    def __init__(self):
        self.subscribers = []
        self.books = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def add_book(self, book):
        self.books.append(book)
        self.notify_subscribers(book)

    def notify_subscribers(self, book):
        for subscriber in self.subscribers:
            subscriber.update(book)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, book):
        print(f"{self.name} has been notified about the new book: {book.title}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library()
john = Subscriber("John Doe")
library.subscribe(john)

new_book = Book("Python Mastery", "Jane Smith")
library.add_book(new_book)

########################################################################################################################

# Python Microservice with 2 endpoints using Flask:
# Flask is the main class for creating a Flask application
# jsonify is to convert Python Dicts to JSON responses
# request is to get data of incoming requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    """Endpoint to return a greeting message"""
    return jsonify({"message": "Hello, welcome to our service!"})

@app.route('/square', methods=['POST'])
def square():
    """Endpoint that squares a number provided by the user"""
    data = request.get_json()
    number = data.get("number", 0)
    return jsonify({"result": number ** 2})

if __name__ == '__main__':
    app.run(debug=True)
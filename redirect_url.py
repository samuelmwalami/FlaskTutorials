from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route('/greet/<person>')
def greet(person):
    return f"<h1>Hello {person}</h1>"

@app.route('/back')
def back():
    return redirect(url_for("greet", person="Sam"))


if __name__ == "__main__":
    app.run()
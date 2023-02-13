from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route('/back')
def back():
    return redirect(url_for("home"))


if __name__ == "__mainn__":
    app.run()
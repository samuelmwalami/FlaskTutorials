from flask import Flask, render_template, redirect, url_for

app = Flask(__name__ ,template_folder='template')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/decision')
def decisions():
    return render_template("decision.html",content="John")

if __name__ == "__main__":
    app.run(debug = True)
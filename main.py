from flask import *
from flask import Flask

app = Flask(__name__)

#routing
@app.route('/home/<name>/<int:age>')
def home(name,age):
    return f"Hello World {name} you are {age} years old"

#using url rule 
def about():
    return "this is the about page"

app.add_url_rule("/about", "about", about)

#url_for

@app.route('/member')
def member():
    return "you are an organization member"

@app.route('/admin')
def admin():
    return "You are the organization's admin"

@app.route('/user/<user>')
def user(user):
    if user == 'member':
        return redirect(url_for('member'))
    if user == 'admin':
        return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug = True, port=5050)
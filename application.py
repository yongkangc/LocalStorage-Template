import os


from flask import Flask, render_template, request,redirect, session
from functools import wraps

# from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# socketio = SocketIO(app)


def login_required(f):
    """
       Decorate routes to require login.

       http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
       """
    @wraps(f)
    def decorated_function(*args, **kwargs):

        #using dict.get() to see if user has logged in
        if not session.get('logged_in'):
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
@login_required
def index():
    return "hi"
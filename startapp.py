#!/usr/bin/env python3

from flask import Flask, render_template, session, redirect, request, url_for
import os
import functools

app = Flask(__name__)
app.secret_key = os.urandom(24)

############################################################################

slova = ("Super", "Perfekt", "Úža", "Flask")


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for("login", url=request.path))

    return wrapper


############################################################################


@app.route("/")
def index():
    return render_template("base.html.j2", slova=slova)


@app.route("/info/")
def info():
    return render_template("info.html.j2")


@app.route("/abc/")
def abc():
    return render_template("abc.html.j2")


@app.route("/text/")
def text():
    return """

<h1>Text</h1>

<p>toto je text</p>

"""


############################################################################
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4444, debug=True)

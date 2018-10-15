#!/usr/bin/env python3
from flask import Flask, render_template, session, redirect, request, url_for
import os
import functools

app = Flask(__name__)
app.secret_key = os.urandom(24)

############################################################################


slova = ('Super', 'Perfekt', 'Úža', 'Flask')


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for('login', url=request.path))
    return wrapper
############################################################################


@app.route('/')
def index():
    return render_template('base.html', slova=slova)


@app.route('/onas/')
def onas():
    return render_template('onas.html')

@app.route("/abc/")
def abc():
    return render_template("abc")


############################################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)



from flask import Flask, render_template, request, redirect, url_for

# UI/CSS
from flask_bootstrap import Bootstrap

# Database
from flask_sqlalchemy import SQLAlchemy

import os
DIR = os.path.dirname(os.path.abspath(__file__))
print(DIR)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)



@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.static_folder = 'static'
    app.debug = True
    app.run()
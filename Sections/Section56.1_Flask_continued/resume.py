import os

DIR = os.path.dirname(os.path.abspath(__file__))

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    # return "<p>Hello, World!</p>"
    return render_template("index.html",name="home_page")

if __name__ == "__main__":
    app.debug = True
    app.run()       

# run in terminal
"""
flask --app resume run
"""

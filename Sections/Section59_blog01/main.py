from flask import Flask, render_template
import requests

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def get_posts():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url )
    print(response.status_code)
    return response.json()



@app.route("/")
def index():
    return render_template("index.html",posts=get_posts())

@app.route("/home")
def home():
    return render_template("index.html",posts=get_posts())

@app.route("/post")
def post():
    return render_template("post.html",posts=get_posts(),num=-1)

@app.route("/post<num>")
def post_num(num):
    return render_template("post.html",posts=get_posts(),num=int(num))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.debug = True
    app.run()    

# run in terminal
"""
flask --app helloflask run
"""

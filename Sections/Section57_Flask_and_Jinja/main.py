from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    rn = random.randint(0,9)
    y = datetime.now().strftime("%Y")
    return render_template("index.html",num=rn, year = y)

@app.route("/blog")
def get_blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url )
    print(response.status_code)
    blog_posts = response.json()

    print(blog_posts)

    return render_template("blog.html",blog_posts=blog_posts,num=-1)


@app.route("/blog/<num>")
def get_post(num):
    print(type(num),num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url )
    # print(response.status_code)
    blog_posts = response.json()

    # print(blog_posts)

    return render_template("blog.html",blog_posts=blog_posts,num=int(num))

if __name__ == "__main__":
    app.debug = True
    app.run()    

# run in terminal
"""
flask --app helloflask run
"""

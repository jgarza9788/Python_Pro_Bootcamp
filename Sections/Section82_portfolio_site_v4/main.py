from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
import requests

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# def get_posts():
#     url = "https://api.npoint.io/c790b4d5cab58020d391"
#     response = requests.get(url )
#     print(response.status_code)
#     return response.json()


@app.route("/")
def index():
    return render_template("test copy 2.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/post<num>")
def post_num(num):
    return render_template("post.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    # if request.method == "POST":
    #     data = request.form
    #     print(data["name"])
    #     print(data["email"])
    #     print(data["phone"])
    #     print(data["message"])

    #     send_email(data)
        
    #     return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")



# send email section

# def send_email(data):
#     import Config
#     cd = Config.Config().data

#     from email.message import EmailMessage
#     import ssl
#     import smtplib

#     em = EmailMessage()
#     em['From'] = cd['email']
#     em['To'] = 'JGarza9788@gmail.com'
#     em['Subject'] = 'contact from website'
#     body = """
#         name: {name}
#         email: {email}
#         phone: {phone}
#         message: {message}
#             """.format(
#                 name=data['name'], 
#                 email=data['email'],
#                 phone=data['phone'],
#                 message=data['message'],
#                 )
#     em.set_content(body)

#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#         smtp.login(cd['email'],cd['password'])
#         smtp.sendmail(
#             em['From'], em['To'], em.as_string()
#             )



if __name__ == "__main__":
    app.debug = True
    app.run()    

# run in terminal
"""
flask --app helloflask run
"""

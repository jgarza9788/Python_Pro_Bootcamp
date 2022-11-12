

from portfolio import portfolio
p = portfolio()

from fuzzywuzzy import fuzz

import re

import time
from flask import Flask, make_response, render_template, request, url_for, redirect, flash, send_from_directory


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
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


# @app.route("/theme")
# @app.route("/theme/<theme>", methods=["GET", "POST"])
@app.route("/theme", methods=["GET", "POST"])
def theme():
    theme = request.form["theme"]
    page =  request.form["page"]
    print(theme,page)
    res = make_response(redirect(url_for(page)))
    res.set_cookie("theme", theme)
    # print(res)
    # return "ok"
    return res


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",portfolio_data=p.data,query="")

@app.route("/portfolio/")
def portfolio_blank():
    return redirect(url_for("portfolio"))

@app.route("/portfolio/<query>", methods=['GET', 'POST'])
def portfolio_query(query):

    print(query)

    if len(query) < 2:
        return redirect(url_for("portfolio"))

    query = query.lower()

    pl = []
    for i in p.data:
        if query in str(i).lower():
            pl.append(i)
        else:
            temp = re.sub(r'[^A-Za-z]+',',',str(i).lower())
            for w in re.split(',',temp):
                # print(w)
                if fuzz.ratio(query, w) > 85:
                    pl.append(i)
                    break;
    
    return render_template("portfolio.html",portfolio_data=pl,query=query)


# @app.route("/portfolio/project")
# def project():
#     return render_template("portfolio.html")



@app.route("/resume")
def resume():
    return render_template("resume.html")


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
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, host= '192.168.182.1', port="8080")
    # app.run(debug=True, host= '192.168.23.1', port="8080")
    app.run(debug=True, host= '192.168.1.130', port="8800")

# run in terminal
"""
flask --app helloflask run
"""

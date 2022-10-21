
#TODO: add sqlite database
#TODO:  add edit page?

from enum import unique
from flask import Flask, render_template, request, redirect, url_for

# UI/CSS
from flask_bootstrap import Bootstrap

# FORMS
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

# Database
from flask_sqlalchemy import SQLAlchemy


import os
DIR = os.path.dirname(os.path.abspath(__file__))
print(DIR)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(DIR,'cafes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + DIR + "cafes.db"
#Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create table

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True,nullable=False) 
    location = db.Column(db.String(2500))
    open = db.Column(db.String(255))
    close = db.Column(db.String(255)) 
    coffee_rating = db.Column(db.String(255))
    wifi_rating = db.Column(db.String(255))
    power_rating = db.Column(db.String(255))

with app.app_context():
    db.create_all()

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    print(all_cafes)
    print(type(all_cafes))
    return render_template('index.html', cafes=all_cafes)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
                name = form.name.data,
                location = form.location.data,
                open = form.open.data,
                close = form.close.data,
                coffee_rating = form.coffee_rating.data,
                wifi_rating = form.wifi_rating.data,
                power_rating = form.power_rating.data
            )
        db.session.add(new_cafe)
        db.session.commit()
        all_cafes = db.session.query(Cafe).all()
        return render_template('index.html', cafes=all_cafes)
    return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    try:
        form = CafeForm()
        cte = Cafe.query.get(id)

        if form.validate_on_submit():

            cte.name = form.name.data
            cte.location = form.location.data
            cte.open = form.open.data
            cte.close = form.close.data
            cte.coffee_rating = form.coffee_rating.data
            cte.wifi_rating = form.wifi_rating.data
            cte.power_rating = form.power_rating.data

            db.session.commit()
            # all_cafes = db.session.query(Cafe).all()
            return redirect(url_for('home'))
    
        else:
            print(id)
            # cafe to edit = cte
            cte = Cafe.query.get(id)
            print(cte)
            print(cte.name)
            form = CafeForm()
            form.name.data = cte.name
            form.location.data = cte.location
            form.open.data = cte.open
            form.close.data = cte.close
            form.coffee_rating.data = cte.coffee_rating
            form.wifi_rating.data = cte.wifi_rating
            form.power_rating.data = cte.power_rating
            return render_template('edit.html', form=form)
    except:
        print('error: id: ', str(id) ,' might not exist')
    return redirect(url_for('home'))

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    try:
        print(id)
        cafe_to_delete = Cafe.query.get(id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
    except:
        print('error: id: ', str(id) ,' not deleted')
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.static_folder = 'static'
    app.debug = True
    app.run()
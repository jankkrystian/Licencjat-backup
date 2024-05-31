import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ...

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_latin = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(100), nullable=False)
    bio_fact = db.Column(db.Text)
    bio_product = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False)
    

    def __repr__(self):
        return f'<Produkt {self.title}>' 
    
# ...

@app.route('/sklepik')
def index():
    products = Product.query.all()
    return render_template('sklepik.html', products=products)    
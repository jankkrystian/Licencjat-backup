import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# ...


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_latin = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    type_title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    bio_fact = db.Column(db.Text)
    bio_info = db.Column(db.Text)
    image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Produkt {self.title}>'
    
# ...

@app.route('/sklepik')
def sklepik():
    products = Product.query.all()
    return render_template('sklepik.html', products=products)    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produkt/<product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('produkt.html', product=product) 

@app.route('/adnotacja')
def adnotacja():
    return render_template('adnotacja.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
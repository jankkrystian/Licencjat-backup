from flask import render_template, request

from models import Product

def register_routes(app, db):

    @app.route('/')
    def index():
        products = Product.query.all()
        return str(products)
    
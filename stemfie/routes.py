from flask import render_template, url_for
from werkzeug.utils import secure_filename

from stemfie import app, db
from .models import Product


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blocks/<str: uuid>')
def product(uuid):
    return render_template('product.html')

@app.route('/category/<str: cat_name>')
def category(cat_name):
    return render_template('category.html')

@app.route('/how-stemfie-platform-works')
def howto():
    return render_template('howto.html')

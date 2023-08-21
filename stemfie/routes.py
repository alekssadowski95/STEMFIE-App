from flask import render_template, url_for, redirect
from sqlalchemy import desc, func

from stemfie import app, db, domain
from .models import Product


@app.route('/')
def home():
    random_product =  Product.query.filter_by(is_active = 1).order_by(func.random()).first()
    featured_beams = Product.query.filter_by(category = 'Beams', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_braces = Product.query.filter_by(category = 'Braces', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_connectors = Product.query.filter_by(category = 'Connectors', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_fasteners = Product.query.filter_by(category = 'Fasteners', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_plates = Product.query.filter_by(category = 'Plates', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_shafts = Product.query.filter_by(category = 'Shafts', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_springs = Product.query.filter_by(category = 'Springs', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    featured_tools = Product.query.filter_by(category = 'Tools', is_active = 1).order_by(desc(Product.relevance)).limit(3)
    return render_template('home.html', random_product = random_product, featured_beams = featured_beams, featured_braces = featured_braces, featured_connectors = featured_connectors, featured_fasteners = featured_fasteners, featured_plates = featured_plates, featured_shafts = featured_shafts, featured_springs = featured_springs, featured_tools = featured_tools)

@app.route('/blocks/<id>')
def product(id):
    # check if id is Integer
    if not isinstance(int(id), int):
        return redirect(url_for('home'))
    product = Product.query.filter_by(id = id).first()
    # increment view count by 1
    product.view_count = product.view_count + 1
    # commit iew count to database
    db.session.commit()
    return render_template('viewer.html', product = product, domain = domain, str = str)

@app.route('/category/<cat_name>')
def category(cat_name):
    # check if category name is valid
    if cat_name not in ('Beams', 'Braces', 'Connectors', 'Fasteners', 'Plates', 'Shafts', 'Springs', 'Tools'):
        return redirect(url_for('home'))
    # get all products with the given category name
    products = Product.query.filter_by(category = cat_name)
    return render_template('category.html', cat_name = cat_name, products = products)

@app.route('/how-stemfie-platform-works')
def howto():
    return render_template('howto.html')

from stemfie import db


class Product(db.Model):
    # required
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    # default
    view_count = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Boolean, nullable=False, default=True)  
    preview_stl_filename = db.Column(db.String(100), nullable=False, default='')
    download_stl_filename = db.Column(db.String(100), nullable=False, default='')

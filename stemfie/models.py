from stemfie import db
import uuid


class Product(db.Model):
    # required
    id = db.Column(db.Integer, primary_key=True)    
    # default
    category = db.Column(db.String(100), nullable=False, default='Uncategorized')
    name = db.Column(db.String(100), nullable=False, default='Unnamed')
    relevance = db.Column(db.Integer, nullable=False, default=50)
    view_count = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Boolean, nullable=False, default=True)  
    preview_img_filename = db.Column(db.String(100), nullable=False, default='default-blocks-preview-img.jpg')
    preview_3d_filename = db.Column(db.String(100), nullable=False, default='default-blocks-preview-3d.stl')
    download_3d_filename = db.Column(db.String(100), nullable=False, default='default-blocks-download-3d.stl')

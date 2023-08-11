from stemfie import db
from stemfie import app

with app.app_context():
    db.create_all()
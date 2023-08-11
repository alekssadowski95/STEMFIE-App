import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# setup project paths
module_path = os.path.abspath(__file__)
module_dir_path = os.path.dirname(module_path)
STL_FILES_DIR_PATH = os.path.join(module_dir_path, 'static', 'content')

# Create flask app instance
application = app = Flask(__name__)

# Add database
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Add secret key
app.config['SECRET_KEY'] = '59f063a2e5406614813c5b07e129fdrb'

# Add routes to app
from stemfie import routes
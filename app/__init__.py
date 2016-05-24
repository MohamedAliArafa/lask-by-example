__author__ = 'fantom'
# Import flask and template operators
from flask import Flask, render_template
import os
from flask_pushjack import FlaskGCM
from flask.ext.login import LoginManager

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# GCM Config
config = {
    'GCM_API_KEY': 'AIzaSyCzQAHq4TuZV8J6YKZvQnyKrNSHyGp-b54'
}
app.config.update(config)

# GCM client Init
client = FlaskGCM()
client.init_app(app)

# Upload Folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top

# Service API-KEY
API_KEY = '627562626c6520617069206b6579'
API_KEY_ERROR = "Invalid API KEY"

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Login Manager Init
login_manager = LoginManager()
login_manager.init_app(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Date handler for Create and Update Date
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

# Import a module / component using its blueprint handler variable (mod_auth)
from app.shopsite.controller import mod_site as site_module
from app.admin.controller import mod_admin as admin_module

# Register blueprint(s)
app.register_blueprint(site_module)
app.register_blueprint(admin_module)
# app.register_blueprint(xyz_module)


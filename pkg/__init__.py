import os
from flask import Flask
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail

csrf = CSRFProtect()
mail = Mail()

def create_app():
    from pkg import config
    from pkg.models import db

    app = Flask(__name__,static_folder='assets') 
    # app.config['SECRET_KEY'] = 'strongsecuredsecretkey' 
    # app.config['ADMIN_EMAIL'] = 'support@gmail.com'

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 
    app.config['ADMIN_EMAIL'] = os.getenv('ADMIN_EMAIL')
    app.config.from_object(config.Config)

    db.init_app(app)
    csrf.init_app(app)
    migrate = Migrate(app,db)
    mail.init_app(app)

    return app
    
app = create_app()

def create_db():
    from pkg.models import db
    with app.app_context():
        db.create_all()

from pkg import routes,forms,db_routes,json_routes,ajax_routes


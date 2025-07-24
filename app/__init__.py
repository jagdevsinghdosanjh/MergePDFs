# import os
# from flask import Flask
# from app.routes import register_routes

# app = Flask(__name__, template_folder=template_dir)
# app.secret_key = 'fc7e97116ab861918317c2c3c11c049f243ef7e77703488b35f80c9ca88cdcdc'  # You can make this stronger

# def create_app():
#     template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
#     app = Flask(__name__, template_folder=template_dir)
#     register_routes(app)
#     return app

import os
from flask import Flask
from app.routes import register_routes

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    
    # SECRET_KEY='fc7e97116ab861918317c2c3c11c049f243ef7e77703488b35f80c9ca88cdcdc'

    # Load secret key from environment
    app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-local-dev')

    register_routes(app)
    return app

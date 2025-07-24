from flask import Flask
from app.routes import register_routes
app = Flask(__name__, template_folder='../templates')


def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

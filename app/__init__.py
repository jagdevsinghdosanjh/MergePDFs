import os
from flask import Flask
from app.routes import register_routes

def create_app():
    # Absolute path to the 'templates' folder
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    register_routes(app)
    return app


# from flask import Flask
# from app.routes import register_routes
# app = Flask(__name__, template_folder='../templates')


# def create_app():
#     app = Flask(__name__)
#     register_routes(app)
#     return app

# import os
# from flask import Flask
# from app.routes import register_routes

# def create_app():
#     app = Flask(__name__, template_folder='templates', static_folder='static')
#     app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-local-dev')
#     register_routes(app)
#     return app

# # import os
# # from flask import Flask
# # from app.routes import register_routes

# # def create_app():
# #     template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
# #     app = Flask(__name__, template_folder=template_dir)

# #     # Load secret key from environment
# #     app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-local-dev')

# #     register_routes(app)
# #     return app

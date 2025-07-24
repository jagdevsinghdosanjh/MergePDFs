# import os
# from flask import Flask
# from app.routes import register_routes

# def create_app():
#     app = Flask(__name__, template_folder='templates', static_folder='static')

#     # Load secret key from environment
#     app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-local-dev')

#     register_routes(app)
#     return app

# import os
# from flask import Flask
# from app.routes import register_routes
# def create_app():
#     template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
#     app = Flask(__name__, template_folder='templates', static_folder='static')

#     # Load secret key from environment
#     app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key-for-local-dev')

#     register_routes(app)
#     return app

from app import create_app
from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

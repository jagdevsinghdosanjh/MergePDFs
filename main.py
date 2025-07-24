from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask
# from app import create_app

# app = Flask(__name__, template_folder='templates')

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

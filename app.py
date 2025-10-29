from flask import Flask
from routes import main_routes  # import blueprint

app = Flask(__name__)
app.register_blueprint(main_routes)  # register routes blueprint

if __name__ == '__main__':
    app.run(debug=True)


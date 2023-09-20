from flask import Flask
from models import db
from routes import main
import json

app = Flask(__name__)
app.secret_key = "manthan"

with open('config.json', 'r') as c:
    params = json.load(c)['params']
local_server = True


if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

db.init_app(app)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

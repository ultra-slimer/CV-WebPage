from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '4xrc68tgv7y870vb0892'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost'
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

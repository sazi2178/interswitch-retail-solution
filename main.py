# Inbuilt libs
import os

#External Libraries
from flask import Flask,request,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#Instantiate App
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello Worls</h1>"

#run statement
if __name__ == '__main__':
	app.run(debug=True,port=5500)
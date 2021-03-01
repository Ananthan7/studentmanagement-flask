from flask import Flask,render_template,request
import sqlite3 as sql
import os
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("base.html")
@app.route('/main')
def result():
		return render_template("main.html")	
if __name__=="__main__":
	app.run()
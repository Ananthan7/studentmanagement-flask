from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import sqlite3 as sql
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enterrow')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            con = sql.connect("database3.db")
            cur = con.cursor()
            cur.execute("INSERT INTO student(Name,Address,City,Pin) VALUES (?,?,?,?);", (nm, addr, city, pin))
            con.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template('result.html', msg=msg)
            con.close


@app.route('/list')
def list():
    con = sql.connect("database3.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall();
    return render_template('list.html', rows=rows)


@app.route('/upload')
def upload_form():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('uploader.html')


if __name__ == '__main__':
    app.run(port=8000)

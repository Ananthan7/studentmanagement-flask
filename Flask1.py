import os
import sqlite3 as sql
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/marks')
def marks():
    return render_template('mark.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        r = request.form
        return render_template('result.html', x=r)

# uploading
@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/addstudent', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']

            con = sql.connect('studentlist.db')
            cur = con.cursor()
            cur.execute("INSERT INTO student(Name,Address,City,Pin) VALUES(?,?,?,?)", (name, address, city, pin))
            con.commit()
            msg = 'recorded successfully'
        except:
            con.rollback()
            msg = "Error in field"

        finally:
            return render_template('done.html', msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect('studentlist.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('select * from student')
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == "POST":
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('uploader.html')


if __name__ == "__main__":
    app.run(port=8000)

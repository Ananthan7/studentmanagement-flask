from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
App.route('Enter row')
def new_student():
    return render_template('student.html')
@app.route('/addrec',method=('POST,GET'))
def addrec():
    if(request.method=='POST'):
        try:
            n=request.form['nm']
            a=request.form['add']
            c=request.form['city']
            p=request.form['pin']
            con=sqlite.connect('database.db')
            cur=con.cursor()
            cur.execute('INSERT INTO student(name,addr,city,pin)VALUES(????)',(n,a,c,p))
            con.commit()
            msg="Record sucessfully added"
        except:
            con.rollback()
            msg="Error in insert operation"
        finally:
            return render_template('result.html')
            
con.close()
@app.route('/list')
def list():
    con=sqlite.connect('database.db')
    cur=con.cursor()
    cur.execute('select * from student')
    rows=cur.fetchall()
    return render_template('list.html',row=rows)
@app.route('/')
def home():
    return render_template('home.html')

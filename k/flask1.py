from flask import Flask
from flask import redirect
from flask import url_for
app=Flask(__name__)
@app.route('/admin')
def hello_admin():
    return 'hello admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s as guest'%guest
@app.route('/user/<name>')
def hello_user(name):
    if(name=='admin'):
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
if (__name__=='__main__'):
    app.run(debug=True)

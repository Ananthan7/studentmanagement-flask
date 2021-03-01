from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_admin():
    return 'hello'
@app.route('/home/<float:n>')
def home(n):
    return "the value is %f"%n

if (__name__=='__main__'):
    app.run(debug=True)

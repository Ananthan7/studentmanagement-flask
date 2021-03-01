from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    # c=['krishna','prabeesh','karthu']
    c = {'Phy': 50, 'Chem': 45, 'Bio': 54}
    return render_template('subject.html', name=c)


if (__name__ == '__main__'):
    app.run(debug=True, port=8080)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Login')


@app.route('/account')
def account():
    return render_template('kaf.html', title='Account')


@app.route('/table')
def table():
    return render_template('kaf2.html', title='table')


if __name__ == '__main__':
    app.run(host="0.0.0.0")

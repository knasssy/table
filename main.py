from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Login')


@app.route('/account')
def account():
    return render_template('kaf.html', title='Account')


if __name__ == '__main__':
    app.run(host="0.0.0.0")

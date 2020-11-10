from flask import Flask, render_template
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Login')


@app.route('/account')
def account():
    return render_template('kaf.html', title='Account')


@app.route('/table')
def table():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf2.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=True)

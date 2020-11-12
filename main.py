from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismodest'


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Login')


@app.route('/account')
def account():
    return render_template('base_kaf.html', title='Account')


# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         teacher = request.form['teacher']
#         platoon = request.form['platoon']
#
#         if not teacher:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (teacher, platoon) VALUES (?, ?)',
#                          (teacher, platoon))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('account'))
#     return render_template('home.html')
# return render_template('create.html')

@app.route('/table1')
def table1():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf1.html', posts=posts)


@app.route('/table2')
def table2():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf2.html', posts=posts)


@app.route('/table3')
def table3():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf3.html', posts=posts)


@app.route('/table4')
def table4():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf4.html', posts=posts)


@app.route('/table5')
def table5():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf5.html', posts=posts)


@app.route('/table6')
def table6():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf6.html', posts=posts)


@app.route('/table11')
def table11():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf11.html', posts=posts)


@app.route('/table12')
def table12():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf12.html', posts=posts)


@app.route('/table13')
def table13():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf13.html', posts=posts)


@app.route('/table21')
def table21():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf21.html', posts=posts)


@app.route('/table22')
def table22():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf22.html', posts=posts)


@app.route('/table23')
def table23():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf23.html', posts=posts)


@app.route('/table31')
def table31():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf31.html', posts=posts)


@app.route('/table32')
def table32():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf32.html', posts=posts)


@app.route('/table33')
def table33():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('kaf33.html', posts=posts)


# TODO ID => GROUP
# @app.route('/table<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     return render_template('kaf21.html', post=post)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=True)

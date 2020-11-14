from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3


# from ftplib import FTP
#
# ftp = FTP()
# HOST = '192.168.255.250'
# PORT = 21
# ftp.connect(HOST, PORT)
# ftp.login(user='ftpuser', passwd='ftpuser21')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


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
    kaf1 = conn.execute('SELECT * FROM kaf1').fetchall()
    conn.close()
    return render_template('kaf1.html', kaf1=kaf1)


@app.route('/table2')
def table2():
    conn = get_db_connection()
    kaf2 = conn.execute('SELECT * FROM kaf2 WHERE id = 1',
                        ).fetchone()
    conn.close()
    return render_template('kaf2.html', kaf2=kaf2)


@app.route('/table3')
def table3():
    conn = get_db_connection()
    kaf3 = conn.execute('SELECT * FROM kaf3').fetchall()
    conn.close()
    return render_template('kaf3.html', kaf3=kaf3)


@app.route('/table4')
def table4():
    conn = get_db_connection()
    kaf4 = conn.execute('SELECT * FROM kaf4').fetchall()
    conn.close()
    return render_template('kaf4.html', kaf4=kaf4)


@app.route('/table5')
def table5():
    conn = get_db_connection()
    kaf5 = conn.execute('SELECT * FROM kaf5').fetchall()
    conn.close()
    return render_template('kaf5.html', kaf5=kaf5)


@app.route('/table6')
def table6():
    conn = get_db_connection()
    kaf6 = conn.execute('SELECT * FROM kaf6').fetchall()
    conn.close()
    return render_template('kaf6.html', kaf6=kaf6)


@app.route('/table11')
def table11():
    conn = get_db_connection()
    kaf11 = conn.execute('SELECT * FROM kaf11').fetchall()
    conn.close()
    return render_template('kaf11.html', kaf11=kaf11)


@app.route('/table12')
def table12():
    conn = get_db_connection()
    kaf12 = conn.execute('SELECT * FROM kaf12').fetchall()
    conn.close()
    return render_template('kaf12.html', kaf12=kaf12)


@app.route('/table13')
def table13():
    conn = get_db_connection()
    kaf13 = conn.execute('SELECT * FROM kaf13').fetchall()
    conn.close()
    return render_template('kaf13.html', kaf13=kaf13)


@app.route('/table21')
def table21():
    conn = get_db_connection()
    # 1 class
    kaf21_1 = conn.execute('SELECT * FROM kaf21 WHERE id = 1').fetchone()
    kaf21_2 = conn.execute('SELECT * FROM kaf21 WHERE id = 2').fetchone()
    kaf21_3 = conn.execute('SELECT * FROM kaf21 WHERE id = 3').fetchone()
    kaf21_4 = conn.execute('SELECT * FROM kaf21 WHERE id = 4').fetchone()
    kaf21_5 = conn.execute('SELECT * FROM kaf21 WHERE id = 5').fetchone()
    # 2 class
    kaf21_6 = conn.execute('SELECT * FROM kaf21 WHERE id = 6').fetchone()
    kaf21_7 = conn.execute('SELECT * FROM kaf21 WHERE id = 7').fetchone()
    kaf21_8 = conn.execute('SELECT * FROM kaf21 WHERE id = 8').fetchone()
    kaf21_9 = conn.execute('SELECT * FROM kaf21 WHERE id = 9').fetchone()
    kaf21_10 = conn.execute('SELECT * FROM kaf21 WHERE id = 10').fetchone()
    # 3 class
    kaf21_11 = conn.execute('SELECT * FROM kaf21 WHERE id = 11').fetchone()
    kaf21_12 = conn.execute('SELECT * FROM kaf21 WHERE id = 12').fetchone()
    kaf21_13 = conn.execute('SELECT * FROM kaf21 WHERE id = 13').fetchone()
    kaf21_14 = conn.execute('SELECT * FROM kaf21 WHERE id = 14').fetchone()
    kaf21_15 = conn.execute('SELECT * FROM kaf21 WHERE id = 15').fetchone()
    # 4 class
    kaf21_16 = conn.execute('SELECT * FROM kaf21 WHERE id = 16').fetchone()
    kaf21_17 = conn.execute('SELECT * FROM kaf21 WHERE id = 17').fetchone()
    kaf21_18 = conn.execute('SELECT * FROM kaf21 WHERE id = 18').fetchone()
    kaf21_19 = conn.execute('SELECT * FROM kaf21 WHERE id = 19').fetchone()
    kaf21_20 = conn.execute('SELECT * FROM kaf21 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf21.html', kaf21_1=kaf21_1, kaf21_2=kaf21_2,
                           kaf21_3=kaf21_3, kaf21_4=kaf21_4, kaf21_5=kaf21_5,
                           kaf21_6=kaf21_6, kaf21_7=kaf21_7, kaf21_8=kaf21_8,
                           kaf21_9=kaf21_9, kaf21_10=kaf21_10, kaf21_11=kaf21_11,
                           kaf21_12=kaf21_12, kaf21_13=kaf21_13, kaf21_14=kaf21_14,
                           kaf21_15=kaf21_15, kaf21_16=kaf21_16, kaf21_17=kaf21_17,
                           kaf21_18=kaf21_18, kaf21_19=kaf21_19, kaf21_20=kaf21_20)


@app.route('/table22')
def table22():
    conn = get_db_connection()
    kaf22 = conn.execute('SELECT * FROM kaf22').fetchall()
    conn.close()
    return render_template('kaf22.html', kaf22=kaf22)


@app.route('/table23')
def table23():
    conn = get_db_connection()
    kaf23 = conn.execute('SELECT * FROM kaf23').fetchall()
    conn.close()
    return render_template('kaf23.html', kaf23=kaf23)


@app.route('/table31')
def table31():
    conn = get_db_connection()
    kaf31 = conn.execute('SELECT * FROM kaf31').fetchall()
    conn.close()
    return render_template('kaf31.html', kaf31=kaf31)


@app.route('/table32')
def table32():
    conn = get_db_connection()
    kaf32 = conn.execute('SELECT * FROM kaf32').fetchall()
    conn.close()
    return render_template('kaf32.html', kaf32=kaf32)


@app.route('/table33')
def table33():
    conn = get_db_connection()
    kaf33 = conn.execute('SELECT * FROM kaf33').fetchall()
    conn.close()
    return render_template('kaf33.html', kaf33=kaf33)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=True)

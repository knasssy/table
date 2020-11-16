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
    # 1 class
    kaf1_1 = conn.execute('SELECT * FROM kaf1 WHERE id = 1').fetchone()
    kaf1_2 = conn.execute('SELECT * FROM kaf1 WHERE id = 2').fetchone()
    kaf1_3 = conn.execute('SELECT * FROM kaf1 WHERE id = 3').fetchone()
    kaf1_4 = conn.execute('SELECT * FROM kaf1 WHERE id = 4').fetchone()
    kaf1_5 = conn.execute('SELECT * FROM kaf1 WHERE id = 5').fetchone()
    # 2 class
    kaf1_6 = conn.execute('SELECT * FROM kaf1 WHERE id = 6').fetchone()
    kaf1_7 = conn.execute('SELECT * FROM kaf1 WHERE id = 7').fetchone()
    kaf1_8 = conn.execute('SELECT * FROM kaf1 WHERE id = 8').fetchone()
    kaf1_9 = conn.execute('SELECT * FROM kaf1 WHERE id = 9').fetchone()
    kaf1_10 = conn.execute('SELECT * FROM kaf1 WHERE id = 10').fetchone()
    # 3 class
    kaf1_11 = conn.execute('SELECT * FROM kaf1 WHERE id = 11').fetchone()
    kaf1_12 = conn.execute('SELECT * FROM kaf1 WHERE id = 12').fetchone()
    kaf1_13 = conn.execute('SELECT * FROM kaf1 WHERE id = 13').fetchone()
    kaf1_14 = conn.execute('SELECT * FROM kaf1 WHERE id = 14').fetchone()
    kaf1_15 = conn.execute('SELECT * FROM kaf1 WHERE id = 15').fetchone()
    # 4 class
    kaf1_16 = conn.execute('SELECT * FROM kaf1 WHERE id = 16').fetchone()
    kaf1_17 = conn.execute('SELECT * FROM kaf1 WHERE id = 17').fetchone()
    kaf1_18 = conn.execute('SELECT * FROM kaf1 WHERE id = 18').fetchone()
    kaf1_19 = conn.execute('SELECT * FROM kaf1 WHERE id = 19').fetchone()
    kaf1_20 = conn.execute('SELECT * FROM kaf1 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf1.html', kaf1_1=kaf1_1, kaf1_2=kaf1_2,
                           kaf1_3=kaf1_3, kaf1_4=kaf1_4, kaf1_5=kaf1_5,
                           kaf1_6=kaf1_6, kaf1_7=kaf1_7, kaf1_8=kaf1_8,
                           kaf1_9=kaf1_9, kaf1_10=kaf1_10, kaf1_11=kaf1_11,
                           kaf1_12=kaf1_12, kaf1_13=kaf1_13, kaf1_14=kaf1_14,
                           kaf1_15=kaf1_15, kaf1_16=kaf1_16, kaf1_17=kaf1_17,
                           kaf1_18=kaf1_18, kaf1_19=kaf1_19, kaf1_20=kaf1_20)


@app.route('/table2')
def table2():
    conn = get_db_connection()
    # 1 class
    kaf2_1 = conn.execute('SELECT * FROM kaf2 WHERE id = 1').fetchone()
    kaf2_2 = conn.execute('SELECT * FROM kaf2 WHERE id = 2').fetchone()
    kaf2_3 = conn.execute('SELECT * FROM kaf2 WHERE id = 3').fetchone()
    kaf2_4 = conn.execute('SELECT * FROM kaf2 WHERE id = 4').fetchone()
    kaf2_5 = conn.execute('SELECT * FROM kaf2 WHERE id = 5').fetchone()
    # 2 class
    kaf2_6 = conn.execute('SELECT * FROM kaf2 WHERE id = 6').fetchone()
    kaf2_7 = conn.execute('SELECT * FROM kaf2 WHERE id = 7').fetchone()
    kaf2_8 = conn.execute('SELECT * FROM kaf2 WHERE id = 8').fetchone()
    kaf2_9 = conn.execute('SELECT * FROM kaf2 WHERE id = 9').fetchone()
    kaf2_10 = conn.execute('SELECT * FROM kaf2 WHERE id = 10').fetchone()
    # 3 class
    kaf2_11 = conn.execute('SELECT * FROM kaf2 WHERE id = 11').fetchone()
    kaf2_12 = conn.execute('SELECT * FROM kaf2 WHERE id = 12').fetchone()
    kaf2_13 = conn.execute('SELECT * FROM kaf2 WHERE id = 13').fetchone()
    kaf2_14 = conn.execute('SELECT * FROM kaf2 WHERE id = 14').fetchone()
    kaf2_15 = conn.execute('SELECT * FROM kaf2 WHERE id = 15').fetchone()
    # 4 class
    kaf2_16 = conn.execute('SELECT * FROM kaf2 WHERE id = 16').fetchone()
    kaf2_17 = conn.execute('SELECT * FROM kaf2 WHERE id = 17').fetchone()
    kaf2_18 = conn.execute('SELECT * FROM kaf2 WHERE id = 18').fetchone()
    kaf2_19 = conn.execute('SELECT * FROM kaf2 WHERE id = 19').fetchone()
    kaf2_20 = conn.execute('SELECT * FROM kaf2 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf2.html', kaf2_1=kaf2_1, kaf2_2=kaf2_2,
                           kaf2_3=kaf2_3, kaf2_4=kaf2_4, kaf2_5=kaf2_5,
                           kaf2_6=kaf2_6, kaf2_7=kaf2_7, kaf2_8=kaf2_8,
                           kaf2_9=kaf2_9, kaf2_10=kaf2_10, kaf2_11=kaf2_11,
                           kaf2_12=kaf2_12, kaf2_13=kaf2_13, kaf2_14=kaf2_14,
                           kaf2_15=kaf2_15, kaf2_16=kaf2_16, kaf2_17=kaf2_17,
                           kaf2_18=kaf2_18, kaf2_19=kaf2_19, kaf2_20=kaf2_20)


@app.route('/table3')
def table3():
    conn = get_db_connection()
    # 1 class
    kaf3_1 = conn.execute('SELECT * FROM kaf3 WHERE id = 1').fetchone()
    kaf3_2 = conn.execute('SELECT * FROM kaf3 WHERE id = 2').fetchone()
    kaf3_3 = conn.execute('SELECT * FROM kaf3 WHERE id = 3').fetchone()
    kaf3_4 = conn.execute('SELECT * FROM kaf3 WHERE id = 4').fetchone()
    kaf3_5 = conn.execute('SELECT * FROM kaf3 WHERE id = 5').fetchone()
    # 2 class
    kaf3_6 = conn.execute('SELECT * FROM kaf3 WHERE id = 6').fetchone()
    kaf3_7 = conn.execute('SELECT * FROM kaf3 WHERE id = 7').fetchone()
    kaf3_8 = conn.execute('SELECT * FROM kaf3 WHERE id = 8').fetchone()
    kaf3_9 = conn.execute('SELECT * FROM kaf3 WHERE id = 9').fetchone()
    kaf3_10 = conn.execute('SELECT * FROM kaf3 WHERE id = 10').fetchone()
    # 3 class
    kaf3_11 = conn.execute('SELECT * FROM kaf3 WHERE id = 11').fetchone()
    kaf3_12 = conn.execute('SELECT * FROM kaf3 WHERE id = 12').fetchone()
    kaf3_13 = conn.execute('SELECT * FROM kaf3 WHERE id = 13').fetchone()
    kaf3_14 = conn.execute('SELECT * FROM kaf3 WHERE id = 14').fetchone()
    kaf3_15 = conn.execute('SELECT * FROM kaf3 WHERE id = 15').fetchone()
    # 4 class
    kaf3_16 = conn.execute('SELECT * FROM kaf3 WHERE id = 16').fetchone()
    kaf3_17 = conn.execute('SELECT * FROM kaf3 WHERE id = 17').fetchone()
    kaf3_18 = conn.execute('SELECT * FROM kaf3 WHERE id = 18').fetchone()
    kaf3_19 = conn.execute('SELECT * FROM kaf3 WHERE id = 19').fetchone()
    kaf3_20 = conn.execute('SELECT * FROM kaf3 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf3.html', kaf3_1=kaf3_1, kaf3_2=kaf3_2,
                           kaf3_3=kaf3_3, kaf3_4=kaf3_4, kaf3_5=kaf3_5,
                           kaf3_6=kaf3_6, kaf3_7=kaf3_7, kaf3_8=kaf3_8,
                           kaf3_9=kaf3_9, kaf3_10=kaf3_10, kaf3_11=kaf3_11,
                           kaf3_12=kaf3_12, kaf3_13=kaf3_13, kaf3_14=kaf3_14,
                           kaf3_15=kaf3_15, kaf3_16=kaf3_16, kaf3_17=kaf3_17,
                           kaf3_18=kaf3_18, kaf3_19=kaf3_19, kaf3_20=kaf3_20)


@app.route('/table4')
def table4():
    conn = get_db_connection()
    # 1 class
    kaf4_1 = conn.execute('SELECT * FROM kaf4 WHERE id = 1').fetchone()
    kaf4_2 = conn.execute('SELECT * FROM kaf4 WHERE id = 2').fetchone()
    kaf4_3 = conn.execute('SELECT * FROM kaf4 WHERE id = 3').fetchone()
    kaf4_4 = conn.execute('SELECT * FROM kaf4 WHERE id = 4').fetchone()
    kaf4_5 = conn.execute('SELECT * FROM kaf4 WHERE id = 5').fetchone()
    # 2 class
    kaf4_6 = conn.execute('SELECT * FROM kaf4 WHERE id = 6').fetchone()
    kaf4_7 = conn.execute('SELECT * FROM kaf4 WHERE id = 7').fetchone()
    kaf4_8 = conn.execute('SELECT * FROM kaf4 WHERE id = 8').fetchone()
    kaf4_9 = conn.execute('SELECT * FROM kaf4 WHERE id = 9').fetchone()
    kaf4_10 = conn.execute('SELECT * FROM kaf4 WHERE id = 10').fetchone()
    # 3 class
    kaf4_11 = conn.execute('SELECT * FROM kaf4 WHERE id = 11').fetchone()
    kaf4_12 = conn.execute('SELECT * FROM kaf4 WHERE id = 12').fetchone()
    kaf4_13 = conn.execute('SELECT * FROM kaf4 WHERE id = 13').fetchone()
    kaf4_14 = conn.execute('SELECT * FROM kaf4 WHERE id = 14').fetchone()
    kaf4_15 = conn.execute('SELECT * FROM kaf4 WHERE id = 15').fetchone()
    # 4 class
    kaf4_16 = conn.execute('SELECT * FROM kaf4 WHERE id = 16').fetchone()
    kaf4_17 = conn.execute('SELECT * FROM kaf4 WHERE id = 17').fetchone()
    kaf4_18 = conn.execute('SELECT * FROM kaf4 WHERE id = 18').fetchone()
    kaf4_19 = conn.execute('SELECT * FROM kaf4 WHERE id = 19').fetchone()
    kaf4_20 = conn.execute('SELECT * FROM kaf4 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf4.html', kaf4_1=kaf4_1, kaf4_2=kaf4_2,
                           kaf4_3=kaf4_3, kaf4_4=kaf4_4, kaf4_5=kaf4_5,
                           kaf4_6=kaf4_6, kaf4_7=kaf4_7, kaf4_8=kaf4_8,
                           kaf4_9=kaf4_9, kaf4_10=kaf4_10, kaf4_11=kaf4_11,
                           kaf4_12=kaf4_12, kaf4_13=kaf4_13, kaf4_14=kaf4_14,
                           kaf4_15=kaf4_15, kaf4_16=kaf4_16, kaf4_17=kaf4_17,
                           kaf4_18=kaf4_18, kaf4_19=kaf4_19, kaf4_20=kaf4_20)


@app.route('/table5')
def table5():
    conn = get_db_connection()
    # 1 class
    kaf5_1 = conn.execute('SELECT * FROM kaf5 WHERE id = 1').fetchone()
    kaf5_2 = conn.execute('SELECT * FROM kaf5 WHERE id = 2').fetchone()
    kaf5_3 = conn.execute('SELECT * FROM kaf5 WHERE id = 3').fetchone()
    kaf5_4 = conn.execute('SELECT * FROM kaf5 WHERE id = 4').fetchone()
    kaf5_5 = conn.execute('SELECT * FROM kaf5 WHERE id = 5').fetchone()
    # 2 class
    kaf5_6 = conn.execute('SELECT * FROM kaf5 WHERE id = 6').fetchone()
    kaf5_7 = conn.execute('SELECT * FROM kaf5 WHERE id = 7').fetchone()
    kaf5_8 = conn.execute('SELECT * FROM kaf5 WHERE id = 8').fetchone()
    kaf5_9 = conn.execute('SELECT * FROM kaf5 WHERE id = 9').fetchone()
    kaf5_10 = conn.execute('SELECT * FROM kaf5 WHERE id = 10').fetchone()
    # 3 class
    kaf5_11 = conn.execute('SELECT * FROM kaf5 WHERE id = 11').fetchone()
    kaf5_12 = conn.execute('SELECT * FROM kaf5 WHERE id = 12').fetchone()
    kaf5_13 = conn.execute('SELECT * FROM kaf5 WHERE id = 13').fetchone()
    kaf5_14 = conn.execute('SELECT * FROM kaf5 WHERE id = 14').fetchone()
    kaf5_15 = conn.execute('SELECT * FROM kaf5 WHERE id = 15').fetchone()
    # 4 class
    kaf5_16 = conn.execute('SELECT * FROM kaf5 WHERE id = 16').fetchone()
    kaf5_17 = conn.execute('SELECT * FROM kaf5 WHERE id = 17').fetchone()
    kaf5_18 = conn.execute('SELECT * FROM kaf5 WHERE id = 18').fetchone()
    kaf5_19 = conn.execute('SELECT * FROM kaf5 WHERE id = 19').fetchone()
    kaf5_20 = conn.execute('SELECT * FROM kaf5 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf5.html', kaf5_1=kaf5_1, kaf5_2=kaf5_2,
                           kaf5_3=kaf5_3, kaf5_4=kaf5_4, kaf5_5=kaf5_5,
                           kaf5_6=kaf5_6, kaf5_7=kaf5_7, kaf5_8=kaf5_8,
                           kaf5_9=kaf5_9, kaf5_10=kaf5_10, kaf5_11=kaf5_11,
                           kaf5_12=kaf5_12, kaf5_13=kaf5_13, kaf5_14=kaf5_14,
                           kaf5_15=kaf5_15, kaf5_16=kaf5_16, kaf5_17=kaf5_17,
                           kaf5_18=kaf5_18, kaf5_19=kaf5_19, kaf5_20=kaf5_20)


@app.route('/table6')
def table6():
    conn = get_db_connection()
    # 1 class
    kaf6_1 = conn.execute('SELECT * FROM kaf6 WHERE id = 1').fetchone()
    kaf6_2 = conn.execute('SELECT * FROM kaf6 WHERE id = 2').fetchone()
    kaf6_3 = conn.execute('SELECT * FROM kaf6 WHERE id = 3').fetchone()
    kaf6_4 = conn.execute('SELECT * FROM kaf6 WHERE id = 4').fetchone()
    kaf6_5 = conn.execute('SELECT * FROM kaf6 WHERE id = 5').fetchone()
    # 2 class
    kaf6_6 = conn.execute('SELECT * FROM kaf6 WHERE id = 6').fetchone()
    kaf6_7 = conn.execute('SELECT * FROM kaf6 WHERE id = 7').fetchone()
    kaf6_8 = conn.execute('SELECT * FROM kaf6 WHERE id = 8').fetchone()
    kaf6_9 = conn.execute('SELECT * FROM kaf6 WHERE id = 9').fetchone()
    kaf6_10 = conn.execute('SELECT * FROM kaf6 WHERE id = 10').fetchone()
    # 3 class
    kaf6_11 = conn.execute('SELECT * FROM kaf6 WHERE id = 11').fetchone()
    kaf6_12 = conn.execute('SELECT * FROM kaf6 WHERE id = 12').fetchone()
    kaf6_13 = conn.execute('SELECT * FROM kaf6 WHERE id = 13').fetchone()
    kaf6_14 = conn.execute('SELECT * FROM kaf6 WHERE id = 14').fetchone()
    kaf6_15 = conn.execute('SELECT * FROM kaf6 WHERE id = 15').fetchone()
    # 4 class
    kaf6_16 = conn.execute('SELECT * FROM kaf6 WHERE id = 16').fetchone()
    kaf6_17 = conn.execute('SELECT * FROM kaf6 WHERE id = 17').fetchone()
    kaf6_18 = conn.execute('SELECT * FROM kaf6 WHERE id = 18').fetchone()
    kaf6_19 = conn.execute('SELECT * FROM kaf6 WHERE id = 19').fetchone()
    kaf6_20 = conn.execute('SELECT * FROM kaf6 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf6.html', kaf6_1=kaf6_1, kaf6_2=kaf6_2,
                           kaf6_3=kaf6_3, kaf6_4=kaf6_4, kaf6_5=kaf6_5,
                           kaf6_6=kaf6_6, kaf6_7=kaf6_7, kaf6_8=kaf6_8,
                           kaf6_9=kaf6_9, kaf6_10=kaf6_10, kaf6_11=kaf6_11,
                           kaf6_12=kaf6_12, kaf6_13=kaf6_13, kaf6_14=kaf6_14,
                           kaf6_15=kaf6_15, kaf6_16=kaf6_16, kaf6_17=kaf6_17,
                           kaf6_18=kaf6_18, kaf6_19=kaf6_19, kaf6_20=kaf6_20)


@app.route('/table11')
def table11():
    conn = get_db_connection()
    # 1 class
    kaf11_1 = conn.execute('SELECT * FROM kaf11 WHERE id = 1').fetchone()
    kaf11_2 = conn.execute('SELECT * FROM kaf11 WHERE id = 2').fetchone()
    kaf11_3 = conn.execute('SELECT * FROM kaf11 WHERE id = 3').fetchone()
    kaf11_4 = conn.execute('SELECT * FROM kaf11 WHERE id = 4').fetchone()
    kaf11_5 = conn.execute('SELECT * FROM kaf11 WHERE id = 5').fetchone()
    # 2 class
    kaf11_6 = conn.execute('SELECT * FROM kaf11 WHERE id = 6').fetchone()
    kaf11_7 = conn.execute('SELECT * FROM kaf11 WHERE id = 7').fetchone()
    kaf11_8 = conn.execute('SELECT * FROM kaf11 WHERE id = 8').fetchone()
    kaf11_9 = conn.execute('SELECT * FROM kaf11 WHERE id = 9').fetchone()
    kaf11_10 = conn.execute('SELECT * FROM kaf11 WHERE id = 10').fetchone()
    # 3 class
    kaf11_11 = conn.execute('SELECT * FROM kaf11 WHERE id = 11').fetchone()
    kaf11_12 = conn.execute('SELECT * FROM kaf11 WHERE id = 12').fetchone()
    kaf11_13 = conn.execute('SELECT * FROM kaf11 WHERE id = 13').fetchone()
    kaf11_14 = conn.execute('SELECT * FROM kaf11 WHERE id = 14').fetchone()
    kaf11_15 = conn.execute('SELECT * FROM kaf11 WHERE id = 15').fetchone()
    # 4 class
    kaf11_16 = conn.execute('SELECT * FROM kaf11 WHERE id = 16').fetchone()
    kaf11_17 = conn.execute('SELECT * FROM kaf11 WHERE id = 17').fetchone()
    kaf11_18 = conn.execute('SELECT * FROM kaf11 WHERE id = 18').fetchone()
    kaf11_19 = conn.execute('SELECT * FROM kaf11 WHERE id = 19').fetchone()
    kaf11_20 = conn.execute('SELECT * FROM kaf11 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf11.html', kaf11_1=kaf11_1, kaf11_2=kaf11_2,
                           kaf11_3=kaf11_3, kaf11_4=kaf11_4, kaf11_5=kaf11_5,
                           kaf11_6=kaf11_6, kaf11_7=kaf11_7, kaf11_8=kaf11_8,
                           kaf11_9=kaf11_9, kaf11_10=kaf11_10, kaf11_11=kaf11_11,
                           kaf11_12=kaf11_12, kaf11_13=kaf11_13, kaf11_14=kaf11_14,
                           kaf11_15=kaf11_15, kaf11_16=kaf11_16, kaf11_17=kaf11_17,
                           kaf11_18=kaf11_18, kaf11_19=kaf11_19, kaf11_20=kaf11_20)


@app.route('/table12')
def table12():
    conn = get_db_connection()
    # 1 class
    kaf12_1 = conn.execute('SELECT * FROM kaf12 WHERE id = 1').fetchone()
    kaf12_2 = conn.execute('SELECT * FROM kaf12 WHERE id = 2').fetchone()
    kaf12_3 = conn.execute('SELECT * FROM kaf12 WHERE id = 3').fetchone()
    kaf12_4 = conn.execute('SELECT * FROM kaf12 WHERE id = 4').fetchone()
    kaf12_5 = conn.execute('SELECT * FROM kaf12 WHERE id = 5').fetchone()
    # 2 class
    kaf12_6 = conn.execute('SELECT * FROM kaf12 WHERE id = 6').fetchone()
    kaf12_7 = conn.execute('SELECT * FROM kaf12 WHERE id = 7').fetchone()
    kaf12_8 = conn.execute('SELECT * FROM kaf12 WHERE id = 8').fetchone()
    kaf12_9 = conn.execute('SELECT * FROM kaf12 WHERE id = 9').fetchone()
    kaf12_10 = conn.execute('SELECT * FROM kaf12 WHERE id = 10').fetchone()
    # 3 class
    kaf12_11 = conn.execute('SELECT * FROM kaf12 WHERE id = 11').fetchone()
    kaf12_12 = conn.execute('SELECT * FROM kaf12 WHERE id = 12').fetchone()
    kaf12_13 = conn.execute('SELECT * FROM kaf12 WHERE id = 13').fetchone()
    kaf12_14 = conn.execute('SELECT * FROM kaf12 WHERE id = 14').fetchone()
    kaf12_15 = conn.execute('SELECT * FROM kaf12 WHERE id = 15').fetchone()
    # 4 class
    kaf12_16 = conn.execute('SELECT * FROM kaf12 WHERE id = 16').fetchone()
    kaf12_17 = conn.execute('SELECT * FROM kaf12 WHERE id = 17').fetchone()
    kaf12_18 = conn.execute('SELECT * FROM kaf12 WHERE id = 18').fetchone()
    kaf12_19 = conn.execute('SELECT * FROM kaf12 WHERE id = 19').fetchone()
    kaf12_20 = conn.execute('SELECT * FROM kaf12 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf12.html', kaf12_1=kaf12_1, kaf12_2=kaf12_2,
                           kaf12_3=kaf12_3, kaf12_4=kaf12_4, kaf12_5=kaf12_5,
                           kaf12_6=kaf12_6, kaf12_7=kaf12_7, kaf12_8=kaf12_8,
                           kaf12_9=kaf12_9, kaf12_10=kaf12_10, kaf12_11=kaf12_11,
                           kaf12_12=kaf12_12, kaf12_13=kaf12_13, kaf12_14=kaf12_14,
                           kaf12_15=kaf12_15, kaf12_16=kaf12_16, kaf12_17=kaf12_17,
                           kaf12_18=kaf12_18, kaf12_19=kaf12_19, kaf12_20=kaf12_20)


@app.route('/table13')
def table13():
    conn = get_db_connection()
    # 1 class
    kaf13_1 = conn.execute('SELECT * FROM kaf13 WHERE id = 1').fetchone()
    kaf13_2 = conn.execute('SELECT * FROM kaf13 WHERE id = 2').fetchone()
    kaf13_3 = conn.execute('SELECT * FROM kaf13 WHERE id = 3').fetchone()
    kaf13_4 = conn.execute('SELECT * FROM kaf13 WHERE id = 4').fetchone()
    kaf13_5 = conn.execute('SELECT * FROM kaf13 WHERE id = 5').fetchone()
    # 2 class
    kaf13_6 = conn.execute('SELECT * FROM kaf13 WHERE id = 6').fetchone()
    kaf13_7 = conn.execute('SELECT * FROM kaf13 WHERE id = 7').fetchone()
    kaf13_8 = conn.execute('SELECT * FROM kaf13 WHERE id = 8').fetchone()
    kaf13_9 = conn.execute('SELECT * FROM kaf13 WHERE id = 9').fetchone()
    kaf13_10 = conn.execute('SELECT * FROM kaf13 WHERE id = 10').fetchone()
    # 3 class
    kaf13_11 = conn.execute('SELECT * FROM kaf13 WHERE id = 11').fetchone()
    kaf13_12 = conn.execute('SELECT * FROM kaf13 WHERE id = 12').fetchone()
    kaf13_13 = conn.execute('SELECT * FROM kaf13 WHERE id = 13').fetchone()
    kaf13_14 = conn.execute('SELECT * FROM kaf13 WHERE id = 14').fetchone()
    kaf13_15 = conn.execute('SELECT * FROM kaf13 WHERE id = 15').fetchone()
    # 4 class
    kaf13_16 = conn.execute('SELECT * FROM kaf13 WHERE id = 16').fetchone()
    kaf13_17 = conn.execute('SELECT * FROM kaf13 WHERE id = 17').fetchone()
    kaf13_18 = conn.execute('SELECT * FROM kaf13 WHERE id = 18').fetchone()
    kaf13_19 = conn.execute('SELECT * FROM kaf13 WHERE id = 19').fetchone()
    kaf13_20 = conn.execute('SELECT * FROM kaf13 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf13.html', kaf13_1=kaf13_1, kaf13_2=kaf13_2,
                           kaf13_3=kaf13_3, kaf13_4=kaf13_4, kaf13_5=kaf13_5,
                           kaf13_6=kaf13_6, kaf13_7=kaf13_7, kaf13_8=kaf13_8,
                           kaf13_9=kaf13_9, kaf13_10=kaf13_10, kaf13_11=kaf13_11,
                           kaf13_12=kaf13_12, kaf13_13=kaf13_13, kaf13_14=kaf13_14,
                           kaf13_15=kaf13_15, kaf13_16=kaf13_16, kaf13_17=kaf13_17,
                           kaf13_18=kaf13_18, kaf13_19=kaf13_19, kaf13_20=kaf13_20)


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
    # 1 class
    kaf22_1 = conn.execute('SELECT * FROM kaf22 WHERE id = 1').fetchone()
    kaf22_2 = conn.execute('SELECT * FROM kaf22 WHERE id = 2').fetchone()
    kaf22_3 = conn.execute('SELECT * FROM kaf22 WHERE id = 3').fetchone()
    kaf22_4 = conn.execute('SELECT * FROM kaf22 WHERE id = 4').fetchone()
    kaf22_5 = conn.execute('SELECT * FROM kaf22 WHERE id = 5').fetchone()
    # 2 class
    kaf22_6 = conn.execute('SELECT * FROM kaf22 WHERE id = 6').fetchone()
    kaf22_7 = conn.execute('SELECT * FROM kaf22 WHERE id = 7').fetchone()
    kaf22_8 = conn.execute('SELECT * FROM kaf22 WHERE id = 8').fetchone()
    kaf22_9 = conn.execute('SELECT * FROM kaf22 WHERE id = 9').fetchone()
    kaf22_10 = conn.execute('SELECT * FROM kaf22 WHERE id = 10').fetchone()
    # 3 class
    kaf22_11 = conn.execute('SELECT * FROM kaf22 WHERE id = 11').fetchone()
    kaf22_12 = conn.execute('SELECT * FROM kaf22 WHERE id = 12').fetchone()
    kaf22_13 = conn.execute('SELECT * FROM kaf22 WHERE id = 13').fetchone()
    kaf22_14 = conn.execute('SELECT * FROM kaf22 WHERE id = 14').fetchone()
    kaf22_15 = conn.execute('SELECT * FROM kaf22 WHERE id = 15').fetchone()
    # 4 class
    kaf22_16 = conn.execute('SELECT * FROM kaf22 WHERE id = 16').fetchone()
    kaf22_17 = conn.execute('SELECT * FROM kaf22 WHERE id = 17').fetchone()
    kaf22_18 = conn.execute('SELECT * FROM kaf22 WHERE id = 18').fetchone()
    kaf22_19 = conn.execute('SELECT * FROM kaf22 WHERE id = 19').fetchone()
    kaf22_20 = conn.execute('SELECT * FROM kaf22 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf22.html', kaf22_1=kaf22_1, kaf22_2=kaf22_2,
                           kaf22_3=kaf22_3, kaf22_4=kaf22_4, kaf22_5=kaf22_5,
                           kaf22_6=kaf22_6, kaf22_7=kaf22_7, kaf22_8=kaf22_8,
                           kaf22_9=kaf22_9, kaf22_10=kaf22_10, kaf22_11=kaf22_11,
                           kaf22_12=kaf22_12, kaf22_13=kaf22_13, kaf22_14=kaf22_14,
                           kaf22_15=kaf22_15, kaf22_16=kaf22_16, kaf22_17=kaf22_17,
                           kaf22_18=kaf22_18, kaf22_19=kaf22_19, kaf22_20=kaf22_20)


@app.route('/table23')
def table23():
    conn = get_db_connection()
    # 1 class
    kaf23_1 = conn.execute('SELECT * FROM kaf23 WHERE id = 1').fetchone()
    kaf23_2 = conn.execute('SELECT * FROM kaf23 WHERE id = 2').fetchone()
    kaf23_3 = conn.execute('SELECT * FROM kaf23 WHERE id = 3').fetchone()
    kaf23_4 = conn.execute('SELECT * FROM kaf23 WHERE id = 4').fetchone()
    kaf23_5 = conn.execute('SELECT * FROM kaf23 WHERE id = 5').fetchone()
    # 2 class
    kaf23_6 = conn.execute('SELECT * FROM kaf23 WHERE id = 6').fetchone()
    kaf23_7 = conn.execute('SELECT * FROM kaf23 WHERE id = 7').fetchone()
    kaf23_8 = conn.execute('SELECT * FROM kaf23 WHERE id = 8').fetchone()
    kaf23_9 = conn.execute('SELECT * FROM kaf23 WHERE id = 9').fetchone()
    kaf23_10 = conn.execute('SELECT * FROM kaf23 WHERE id = 10').fetchone()
    # 3 class
    kaf23_11 = conn.execute('SELECT * FROM kaf23 WHERE id = 11').fetchone()
    kaf23_12 = conn.execute('SELECT * FROM kaf23 WHERE id = 12').fetchone()
    kaf23_13 = conn.execute('SELECT * FROM kaf23 WHERE id = 13').fetchone()
    kaf23_14 = conn.execute('SELECT * FROM kaf23 WHERE id = 14').fetchone()
    kaf23_15 = conn.execute('SELECT * FROM kaf23 WHERE id = 15').fetchone()
    # 4 class
    kaf23_16 = conn.execute('SELECT * FROM kaf23 WHERE id = 16').fetchone()
    kaf23_17 = conn.execute('SELECT * FROM kaf23 WHERE id = 17').fetchone()
    kaf23_18 = conn.execute('SELECT * FROM kaf23 WHERE id = 18').fetchone()
    kaf23_19 = conn.execute('SELECT * FROM kaf23 WHERE id = 19').fetchone()
    kaf23_20 = conn.execute('SELECT * FROM kaf23 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf23.html', kaf23_1=kaf23_1, kaf23_2=kaf23_2,
                           kaf23_3=kaf23_3, kaf23_4=kaf23_4, kaf23_5=kaf23_5,
                           kaf23_6=kaf23_6, kaf23_7=kaf23_7, kaf23_8=kaf23_8,
                           kaf23_9=kaf23_9, kaf23_10=kaf23_10, kaf23_11=kaf23_11,
                           kaf23_12=kaf23_12, kaf23_13=kaf23_13, kaf23_14=kaf23_14,
                           kaf23_15=kaf23_15, kaf23_16=kaf23_16, kaf23_17=kaf23_17,
                           kaf23_18=kaf23_18, kaf23_19=kaf23_19, kaf23_20=kaf23_20)


@app.route('/table31')
def table31():
    conn = get_db_connection()
    # 1 class
    kaf31_1 = conn.execute('SELECT * FROM kaf31 WHERE id = 1').fetchone()
    kaf31_2 = conn.execute('SELECT * FROM kaf31 WHERE id = 2').fetchone()
    kaf31_3 = conn.execute('SELECT * FROM kaf31 WHERE id = 3').fetchone()
    kaf31_4 = conn.execute('SELECT * FROM kaf31 WHERE id = 4').fetchone()
    kaf31_5 = conn.execute('SELECT * FROM kaf31 WHERE id = 5').fetchone()
    # 2 class
    kaf31_6 = conn.execute('SELECT * FROM kaf31 WHERE id = 6').fetchone()
    kaf31_7 = conn.execute('SELECT * FROM kaf31 WHERE id = 7').fetchone()
    kaf31_8 = conn.execute('SELECT * FROM kaf31 WHERE id = 8').fetchone()
    kaf31_9 = conn.execute('SELECT * FROM kaf31 WHERE id = 9').fetchone()
    kaf31_10 = conn.execute('SELECT * FROM kaf31 WHERE id = 10').fetchone()
    # 3 class
    kaf31_11 = conn.execute('SELECT * FROM kaf31 WHERE id = 11').fetchone()
    kaf31_12 = conn.execute('SELECT * FROM kaf31 WHERE id = 12').fetchone()
    kaf31_13 = conn.execute('SELECT * FROM kaf31 WHERE id = 13').fetchone()
    kaf31_14 = conn.execute('SELECT * FROM kaf31 WHERE id = 14').fetchone()
    kaf31_15 = conn.execute('SELECT * FROM kaf31 WHERE id = 15').fetchone()
    # 4 class
    kaf31_16 = conn.execute('SELECT * FROM kaf31 WHERE id = 16').fetchone()
    kaf31_17 = conn.execute('SELECT * FROM kaf31 WHERE id = 17').fetchone()
    kaf31_18 = conn.execute('SELECT * FROM kaf31 WHERE id = 18').fetchone()
    kaf31_19 = conn.execute('SELECT * FROM kaf31 WHERE id = 19').fetchone()
    kaf31_20 = conn.execute('SELECT * FROM kaf31 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf31.html', kaf31_1=kaf31_1, kaf31_2=kaf31_2,
                           kaf31_3=kaf31_3, kaf31_4=kaf31_4, kaf31_5=kaf31_5,
                           kaf31_6=kaf31_6, kaf31_7=kaf31_7, kaf31_8=kaf31_8,
                           kaf31_9=kaf31_9, kaf31_10=kaf31_10, kaf31_11=kaf31_11,
                           kaf31_12=kaf31_12, kaf31_13=kaf31_13, kaf31_14=kaf31_14,
                           kaf31_15=kaf31_15, kaf31_16=kaf31_16, kaf31_17=kaf31_17,
                           kaf31_18=kaf31_18, kaf31_19=kaf31_19, kaf31_20=kaf31_20)


@app.route('/table32')
def table32():
    conn = get_db_connection()
    # 1 class
    kaf32_1 = conn.execute('SELECT * FROM kaf32 WHERE id = 1').fetchone()
    kaf32_2 = conn.execute('SELECT * FROM kaf32 WHERE id = 2').fetchone()
    kaf32_3 = conn.execute('SELECT * FROM kaf32 WHERE id = 3').fetchone()
    kaf32_4 = conn.execute('SELECT * FROM kaf32 WHERE id = 4').fetchone()
    kaf32_5 = conn.execute('SELECT * FROM kaf32 WHERE id = 5').fetchone()
    # 2 class
    kaf32_6 = conn.execute('SELECT * FROM kaf32 WHERE id = 6').fetchone()
    kaf32_7 = conn.execute('SELECT * FROM kaf32 WHERE id = 7').fetchone()
    kaf32_8 = conn.execute('SELECT * FROM kaf32 WHERE id = 8').fetchone()
    kaf32_9 = conn.execute('SELECT * FROM kaf32 WHERE id = 9').fetchone()
    kaf32_10 = conn.execute('SELECT * FROM kaf32 WHERE id = 10').fetchone()
    # 3 class
    kaf32_11 = conn.execute('SELECT * FROM kaf32 WHERE id = 11').fetchone()
    kaf32_12 = conn.execute('SELECT * FROM kaf32 WHERE id = 12').fetchone()
    kaf32_13 = conn.execute('SELECT * FROM kaf32 WHERE id = 13').fetchone()
    kaf32_14 = conn.execute('SELECT * FROM kaf32 WHERE id = 14').fetchone()
    kaf32_15 = conn.execute('SELECT * FROM kaf32 WHERE id = 15').fetchone()
    # 4 class
    kaf32_16 = conn.execute('SELECT * FROM kaf32 WHERE id = 16').fetchone()
    kaf32_17 = conn.execute('SELECT * FROM kaf32 WHERE id = 17').fetchone()
    kaf32_18 = conn.execute('SELECT * FROM kaf32 WHERE id = 18').fetchone()
    kaf32_19 = conn.execute('SELECT * FROM kaf32 WHERE id = 19').fetchone()
    kaf32_20 = conn.execute('SELECT * FROM kaf32 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf32.html', kaf32_1=kaf32_1, kaf32_2=kaf32_2,
                           kaf32_3=kaf32_3, kaf32_4=kaf32_4, kaf32_5=kaf32_5,
                           kaf32_6=kaf32_6, kaf32_7=kaf32_7, kaf32_8=kaf32_8,
                           kaf32_9=kaf32_9, kaf32_10=kaf32_10, kaf32_11=kaf32_11,
                           kaf32_12=kaf32_12, kaf32_13=kaf32_13, kaf32_14=kaf32_14,
                           kaf32_15=kaf32_15, kaf32_16=kaf32_16, kaf32_17=kaf32_17,
                           kaf32_18=kaf32_18, kaf32_19=kaf32_19, kaf32_20=kaf32_20)


@app.route('/table33')
def table33():
    conn = get_db_connection()
    # 1 class
    kaf33_1 = conn.execute('SELECT * FROM kaf33 WHERE id = 1').fetchone()
    kaf33_2 = conn.execute('SELECT * FROM kaf33 WHERE id = 2').fetchone()
    kaf33_3 = conn.execute('SELECT * FROM kaf33 WHERE id = 3').fetchone()
    kaf33_4 = conn.execute('SELECT * FROM kaf33 WHERE id = 4').fetchone()
    kaf33_5 = conn.execute('SELECT * FROM kaf33 WHERE id = 5').fetchone()
    # 2 class
    kaf33_6 = conn.execute('SELECT * FROM kaf33 WHERE id = 6').fetchone()
    kaf33_7 = conn.execute('SELECT * FROM kaf33 WHERE id = 7').fetchone()
    kaf33_8 = conn.execute('SELECT * FROM kaf33 WHERE id = 8').fetchone()
    kaf33_9 = conn.execute('SELECT * FROM kaf33 WHERE id = 9').fetchone()
    kaf33_10 = conn.execute('SELECT * FROM kaf33 WHERE id = 10').fetchone()
    # 3 class
    kaf33_11 = conn.execute('SELECT * FROM kaf33 WHERE id = 11').fetchone()
    kaf33_12 = conn.execute('SELECT * FROM kaf33 WHERE id = 12').fetchone()
    kaf33_13 = conn.execute('SELECT * FROM kaf33 WHERE id = 13').fetchone()
    kaf33_14 = conn.execute('SELECT * FROM kaf33 WHERE id = 14').fetchone()
    kaf33_15 = conn.execute('SELECT * FROM kaf33 WHERE id = 15').fetchone()
    # 4 class
    kaf33_16 = conn.execute('SELECT * FROM kaf33 WHERE id = 16').fetchone()
    kaf33_17 = conn.execute('SELECT * FROM kaf33 WHERE id = 17').fetchone()
    kaf33_18 = conn.execute('SELECT * FROM kaf33 WHERE id = 18').fetchone()
    kaf33_19 = conn.execute('SELECT * FROM kaf33 WHERE id = 19').fetchone()
    kaf33_20 = conn.execute('SELECT * FROM kaf33 WHERE id = 20').fetchone()
    conn.close()
    return render_template('kaf33.html', kaf33_1=kaf33_1, kaf33_2=kaf33_2,
                           kaf33_3=kaf33_3, kaf33_4=kaf33_4, kaf33_5=kaf33_5,
                           kaf33_6=kaf33_6, kaf33_7=kaf33_7, kaf33_8=kaf33_8,
                           kaf33_9=kaf33_9, kaf33_10=kaf33_10, kaf33_11=kaf33_11,
                           kaf33_12=kaf33_12, kaf33_13=kaf33_13, kaf33_14=kaf33_14,
                           kaf33_15=kaf33_15, kaf33_16=kaf33_16, kaf33_17=kaf33_17,
                           kaf33_18=kaf33_18, kaf33_19=kaf33_19, kaf33_20=kaf33_20)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=True)

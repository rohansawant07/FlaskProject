from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
app.secret_key = "rohan_sawant"

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'MyDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def Index():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM user_table')
    data = cur.fetchall()

    cur.close()
    return render_template('index.html', user_table=data)


@app.route('/add_contact', methods=['POST','GET'])
def add_employee():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        companyname = request.form['companyname']
        phone = request.form['phone']

        cur.execute("INSERT INTO user_table (email,fullname,companyname, phone) VALUES (%s,%s,%s,%s)", (email,fullname, companyname, phone))
        conn.commit()
        return 'Employee Added successfully'
    return redirect('templates/index.html')


@app.route('/edit/<email>', methods=['POST', 'GET'])
def get_employee(email):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM user_table WHERE email = %s', (email))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', user_table=data[0])


@app.route('/update/<email>', methods=['POST'])
def update_employee(email):
    if request.method == 'POST':
        fullname = request.form['fullname']
        companyname=request.form['companyname']
        phone = request.form['phone']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE user_table
            SET fullname = %s,
                companyname = %s,
                phone = %s
            WHERE email = %s
        """, (fullname, companyname, phone, email))
        flash('Employee Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<email>', methods=['POST', 'GET'])
def delete_employee(email):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('DELETE FROM user_table WHERE email = %s', (email))
    conn.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('Index'))


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)

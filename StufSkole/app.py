from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'odatabase'

mysql=MySQL(app)

@app.route('/StufSkole/')
def login():
    msg='Skriv inn brukernavn og passord'
    if request.method == 'POST' and 'username' in request.form and 'user_password' in request.form: #sjekker om brukernavn og passord variablene eksisterer i databasen
        username = request.form['username']
        user_password = request.form['user_password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute =('SELECT *FROM accounts WHERE username= %s AND user_password = %s',(username,user_password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['username'] = account['username']
            msg = 'Du er logget inn!'
    else: msg ='Feil brukernavn/passord. Prøv igjen eller lag en ny bruker!'
    return render_template('innlogging.html',msg=msg)

def message():
    msg= 'Hei'
    return render_template('innlogging.html',msg=msg)

if __name__ == '__main__':
   app.run()

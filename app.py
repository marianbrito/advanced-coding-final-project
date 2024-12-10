from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__) #app instance
app.secret_key = 'marian123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form ['password']
        cur = mysql.connection.cursor()
        cur.execute(f"select username, password from tbl_users where username = '{username}'")
        user = cur.fetchone()
        cur.close()
        if user and password == user[1]:
            session['username'] = user[0]
            return render_template('welcome.html', username=session['username'])
        else:
            return render_template('login.html', error = 'invalid username or password')
    else:
        return render_template('login.html')
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form ['password']
        cur = mysql.connection.cursor()
        cur.execute(f"insert into tbl_users (username, password) values ('{username}', '{password}')")
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('home.html')


    

    
if __name__ == '__main__':
    app.run(debug=True)
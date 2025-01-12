from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static') 
app.secret_key = 'marian123'

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'flask_users'

mysql = MySQL(app)
    
class database:
    def __init__(self, db):
        self.db = db

    def execute(self, query, parameters=None):
        cur = self.db.connection.cursor()
        cur.execute(query,parameters)
        self.db.connection.commit()
        cur.close()
    
    def fetchall(self, query, parameters=None):
        cur = self.db.connection.cursor()
        cur.execute(query,parameters)
        results = cur.fetchall()
        cur.close()
        return results
    
    def fetchone(self, query, parameters=None):
        cur = self.db.connection.cursor()
        cur.execute(query, parameters)
        results = cur.fetchone()
        cur.close()
        return results
    

class user(database):
     def login(self, username, password):
        query ="SELECT user_id, username, password FROM tbl_users WHERE username = %s AND password = %s"
        user_data = self.fetchone(query, (username,password))
        return user_data
     
     def register(self, username, password):
        insert_query ="INSERT INTO tbl_users (username, password) VALUES (%s, %s)" 
        self.execute(insert_query, (username, password))

        query = "SELECT user_id FROM tbl_users WHERE username = %s"
        user_id = self.fetchone(query,(username,))

        return user_id

class product(database):
    def products(self):
        query = "SELECT product_id, name, price, image FROM tbl_products"
        return self.fetchall(query)

class cart(database):
    def view_cart(self, user_id): 
        query = """SELECT tbl_shopppingcart.cart_id, tbl_products.name, tbl_products.price, tbl_shopppingcart.quantity, tbl_products.image 
                    FROM tbl_shopppingcart 
                    JOIN tbl_products ON tbl_shopppingcart.product_id = tbl_products.product_id WHERE tbl_shopppingcart.user_id = %s"""
        
        return self.fetchall(query, (user_id, ))
    
    def add_to_cart(self, user_id, product_id, quantity):
        select_query = "SELECT cart_id, quantity FROM tbl_shopppingcart WHERE user_id = %s AND product_id = %s"
        cart_item = self.fetchone(select_query, (user_id, product_id))

        if cart_item:
            update_query = "UPDATE tbl_shopppingcart SET quantity = quantity + %s WHERE user_id = %s AND product_id = %s"
            self.execute(update_query,(quantity, user_id, product_id))
            
        else:
            insert_query = "INSERT INTO tbl_shopppingcart (user_id, product_id, quantity) VALUES (%s, %s, %s)"
            self.execute(insert_query, (user_id, product_id, quantity))

        return redirect(url_for('view_cart'))

    def remove_from_cart(self, product_id):
        delete_query = "DELETE FROM tbl_shopppingcart WHERE cart_id = %s"
        return self.execute(delete_query, (product_id, ))

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_class = user(mysql)
        user_login = user_class.login(username, password)

        if user_login:
            session['username'] = user_login[1]
            session['user_id'] = user_login[0]
            return render_template('welcome.html', username=session['username'])
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form ['password']

        user_class = user(mysql)
        user_id = user_class.register(username, password)
        session['username'] = username
        session['user_id'] = user_id  
        return redirect(url_for('login'))
    
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)  
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/products')
def products():
    products_class = product(mysql)
    products = products_class.products()
    return render_template('products.html', products=products)


@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    quantity = int(request.form.get('quantity', 1))

    cart_class = cart(mysql)
    cart_class.add_to_cart(user_id, product_id, quantity)

    return redirect(url_for('view_cart'))


@app.route('/view_cart')
def view_cart():
    if 'username' not in session:
        return redirect(url_for('login'))  

    user_id = session['user_id'] 
    cart_class = cart(mysql)
    cart_items = cart_class.view_cart(user_id)

    total_price = sum(item[2] * item[3] for item in cart_items)  

    return render_template('view_cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/remove_from_cart/<int:product_id>', methods=['GET'])
def remove_from_cart(product_id):
    if 'username' not in session:
        return redirect(url_for('login'))  
    
    cart_class = cart(mysql)
    cart_class.remove_from_cart(product_id)

    return redirect(url_for('view_cart'))

@app.route('/checkout')
def checkout():
    if 'username' not in session:
        return redirect(url_for('login'))  

    user_id = session['user_id']
    cart_class = cart(mysql)
    cart_items = cart_class.view_cart(user_id)

    total_price = sum(item[2] * item[3] for item in cart_items)

    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)


@app.route('/finalize_checkout', methods=['POST'])
def finalize_checkout():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        payment_method = request.form.get('payment')

    if not name or not address or not payment_method:
        return "Please fill out all fields."

    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    cart_class = cart(mysql)
    insert_query = "INSERT INTO tbl_orders (user_id, name, address, payment_method) VALUES (%s, %s, %s, %s)"
    cart_class.execute(insert_query, (user_id, name, address, payment_method))

    delete_query = "DELETE FROM tbl_shopppingcart WHERE user_id = %s"
    cart_class.execute(delete_query, (user_id,))

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, request, redirect, url_for, session
from .models import user, product, cart
from . import mysql

# Function to initialize all the routes
def initialize_routes(app):
    """
    Initializes all the routes for the Flask application.

    Args:
        app: The Flask application instance.
    """

    @app.route('/')
    def home():
        """
        Displays the home page.

        Returns:
            Rendered home page template.
        """
        return render_template('home.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """
        Handles user login by verifying username and password.

        If the request method is POST, verifies the credentials and logs the user in. Otherwise, renders the login page.

        Returns:
            Rendered login page or welcome page on successful login.
        """
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

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """
        Handles user registration.

        If the request method is POST, registers a new user and redirects to the login page.

        Returns:
            Rendered registration page or redirection to login page.
        """
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user_class = user(mysql)
            user_id = user_class.register(username, password)
            session['username'] = username
            session['user_id'] = user_id
            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route('/logout')
    def logout():
        """
        Logs the user out by clearing the session.

        Returns:
            Rendered home page template.
        """
        session.pop('username', None)
        session.pop('user_id', None)
        return render_template('home.html')

    @app.route('/welcome')
    def welcome():
        """
        Renders the welcome page after login.

        Returns:
            Rendered welcome page template.
        """
        return render_template('welcome.html')

    @app.route('/products')
    def products():
        """
        Displays the list of available products.

        Returns:
            Rendered products page with product details.
        """
        products_class = product(mysql)
        products = products_class.products()
        return render_template('products.html', products=products)

    @app.route('/add_to_cart/<int:product_id>', methods=['POST'])
    def add_to_cart(product_id):
        """
        Adds a product to the cart if the user is logged in.

        Args:
            product_id: The ID of the product to add.

        Returns:
            Redirection to the cart view or login page if not logged in.
        """
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))

        quantity = int(request.form.get('quantity', 1))

        cart_class = cart(mysql)
        cart_class.add_to_cart(user_id, product_id, quantity)

        return redirect(url_for('view_cart'))

    @app.route('/view_cart')
    def view_cart():
        """
        Displays the cart with the products added by the user.

        If the user is not logged in, redirects to the login page. Calculates the total price of the items in the cart.

        Returns:
            Rendered cart view template with cart items and total price.
        """
        if 'username' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        cart_class = cart(mysql)
        cart_items = cart_class.view_cart(user_id)

        total_price = sum(item[2] * item[3] for item in cart_items)

        return render_template('view_cart.html', cart_items=cart_items, total_price=total_price)

    @app.route('/remove_from_cart/<int:product_id>', methods=['GET'])
    def remove_from_cart(product_id):
        """
        Removes a product from the cart if the user is logged in.

        Args:
            product_id: The ID of the product to remove.

        Returns:
            Redirection to the cart view or login page if not logged in.
        """
        if 'username' not in session:
            return redirect(url_for('login'))

        cart_class = cart(mysql)
        cart_class.remove_from_cart(product_id)

        return redirect(url_for('view_cart'))

    @app.route('/checkout')
    def checkout():
        """
        Displays the checkout page with cart items and total price.

        If the user is not logged in, redirects to the login page.

        Returns:
            Rendered checkout page template.
        """
        if 'username' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        cart_class = cart(mysql)
        cart_items = cart_class.view_cart(user_id)

        total_price = sum(item[2] * item[3] for item in cart_items)

        return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

    @app.route('/finalize_checkout', methods=['POST'])
    def finalize_checkout():
        """
        Finalizes the checkout process by saving order details and clearing the cart.

        If the user is not logged in, redirects to the login page. If any required field is missing, returns an error message.

        Returns:
            Redirection to the confirmation page or error message.
        """
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
        cart_class.finalize_checkout(user_id, name, address, payment_method)

        return redirect(url_for('confirmation'))

    @app.route('/confirmation')
    def confirmation():
        """
        Renders the confirmation page displaying a confirmation message.

        Returns:
            Rendered confirmation page template.
        """
        return render_template('confirmation.html')

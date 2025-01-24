from . import mysql

class database:
    """
    A base class for interacting with a MySQL database.

    Attributes:
        db: A database connection instance.
    """
    def __init__(self, db):
        """
        Initializes the database connection.

        Args:
            db: The database connection object.
        """
        self.db = db

    def execute(self, query, parameters=None):
        """
        Executes a query and commits the changes to the database.

        Args:
            query: SQL query to be executed.
            parameters: Optional tuple of parameters for the query.
        """
        cur = self.db.connection.cursor()
        cur.execute(query, parameters)
        self.db.connection.commit()
        cur.close()

    def fetchall(self, query, parameters=None):
        """
        Executes a query and fetches all results from the database.

        Args:
            query: SQL query to be executed.
            parameters: Optional tuple of parameters for the query.

        Returns:
            List of all rows fetched from the database.
        """
        cur = self.db.connection.cursor()
        cur.execute(query, parameters)
        results = cur.fetchall()
        cur.close()
        return results

    def fetchone(self, query, parameters=None):
        """
        Executes a query and fetches a single result from the database.

        Args:
            query: SQL query to be executed.
            parameters: Optional tuple of parameters for the query.

        Returns:
            A single row fetched from the database.
        """
        cur = self.db.connection.cursor()
        cur.execute(query, parameters)
        results = cur.fetchone()
        cur.close()
        return results

class user(database):
    """
    A subclass of the database class for user-related operations.
    """
    def login(self, username, password):
        """
        Authenticates a user by verifying the username and password.

        Args:
            username: The username of the user.
            password: The password of the user.

        Returns:
            A tuple containing user data if authentication is successful, otherwise None.
        """
        query = "SELECT user_id, username, password FROM tbl_users WHERE username = %s AND password = %s"
        user_data = self.fetchone(query, (username, password))
        return user_data

    def register(self, username, password):
        """
        Registers a new user by inserting their data into the database.

        Args:
            username: The username of the new user.
            password: The password of the new user.

        Returns:
            The user_id of the newly registered user.
        """
        insert_query = "INSERT INTO tbl_users (username, password) VALUES (%s, %s)"
        self.execute(insert_query, (username, password))

        query = "SELECT user_id FROM tbl_users WHERE username = %s"
        user_id = self.fetchone(query, (username,))
        return user_id

class product(database):
    """
    A subclass of the database class for product-related operations.
    """
    def products(self):
        """
        Retrieves all products from the database.

        Returns:
            A list of all products with their details.
        """
        query = "SELECT product_id, name, price, image FROM tbl_products"
        return self.fetchall(query)

class cart(database):
    """
    A subclass of the database class for cart-related operations.
    """
    def view_cart(self, user_id):
        """
        Retrieves all products in the user's cart.

        Args:
            user_id: The ID of the user.

        Returns:
            A list of all products in the user's cart with their details.
        """
        query = """SELECT tbl_shopppingcart.cart_id, tbl_products.name, tbl_products.price, tbl_shopppingcart.quantity, tbl_products.image \
                    FROM tbl_shopppingcart \
                    JOIN tbl_products ON tbl_shopppingcart.product_id = tbl_products.product_id WHERE tbl_shopppingcart.user_id = %s"""
        return self.fetchall(query, (user_id,))

    def add_to_cart(self, user_id, product_id, quantity):
        """
        Adds a product to the user's cart or updates the quantity if the product already exists.

        Args:
            user_id: The ID of the user.
            product_id: The ID of the product to add.
            quantity: The quantity of the product to add.

        Returns:
            True if the operation is successful.
        """
        select_query = "SELECT cart_id, quantity FROM tbl_shopppingcart WHERE user_id = %s AND product_id = %s"
        cart_item = self.fetchone(select_query, (user_id, product_id))

        if cart_item:
            update_query = "UPDATE tbl_shopppingcart SET quantity = quantity + %s WHERE user_id = %s AND product_id = %s"
            self.execute(update_query, (quantity, user_id, product_id))
        else:
            insert_query = "INSERT INTO tbl_shopppingcart (user_id, product_id, quantity) VALUES (%s, %s, %s)"
            self.execute(insert_query, (user_id, product_id, quantity))

        return True

    def remove_from_cart(self, product_id):
        """
        Removes a product from the user's cart.

        Args:
            product_id: The ID of the product to remove.

        Returns:
            None.
        """
        delete_query = "DELETE FROM tbl_shopppingcart WHERE cart_id = %s"
        self.execute(delete_query, (product_id,))

    def finalize_checkout(self, user_id, name, address, payment_method):
        """
        Finalizes the checkout process by creating an order and clearing the cart.

        Args:
            user_id: The ID of the user.
            name: The name of the user.
            address: The shipping address.
            payment_method: The payment method chosen by the user.

        Returns:
            None.
        """
        insert_query = """ INSERT INTO tbl_orders (user_id, name, address, payment_method) VALUES (%s, %s, %s, %s)"""
        self.execute(insert_query, (user_id, name, address, payment_method))

        delete_query = "DELETE FROM tbl_shopppingcart WHERE user_id = %s"
        self.execute(delete_query, (user_id,))

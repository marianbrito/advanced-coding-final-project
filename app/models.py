from . import mysql 

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

        return True

    def remove_from_cart(self, product_id):
        delete_query = "DELETE FROM tbl_shopppingcart WHERE cart_id = %s"
        return self.execute(delete_query, (product_id, ))


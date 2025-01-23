# ADVANCED CODING FINAL PROJECT
ElectroHub is a Flask e-commerce application developed for the final advanced coding project. The application provides functionality for user registration, login, product browsing, cart management, and checkout.

# Table of Contents
- [Advanced Coding Final Project](#advanced-coding-final-project)
- [Features](#features)
  - [1. User Authentication](#1user-authentication)
  - [2. Product Browsing](#2product-browsing)
  - [3. Cart Management](#3cart-management)
  - [4. Checkout Process](#4checkout-process)
  - [5. Dynamic Web Pages](#5dynamic-web-pages)
  - [6. MySQL Integration](#6mysql-integration)
- [Database Setup](#database-setup)
  - [Create a Database](#create-a-database)
  - [Set Up Values in Config.py](#set-up-the-following-values-in-configpy)
- [Setup Instructions](#setup-instructions)
  - [Requisites](#requisites)
  - [Steps](#steps)
- [Screenshots](#screenshots)
  - [Home Page](#home-page)
  - [Products](#products)
  - [Shopping Cart](#shopping-cart)

## Features

__1.User Authentication:__
 
 -Register and log in to the application.
 
 -Logout functionality.
 
__2.Product Browsing:__

 -View the list of available products.
 
__3.Cart Management:*__

 -Add products to the shopping cart, view the cart, and remove items.
 
__4.Checkout Process:__

-finalize your order filling the form with name, address, and payment information.
 
__5.Dynamic Web Pages:__

 -Templates are rendered dynamically using Flask and Jinja2.
 
__6.MySQL Integration:__

 -Data is handled through a MySQL database.
 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Database Setup

This project uses MySQL as the database. To set up the database:

__Create a database:__

  -Use a tool like phpMyAdmin, MySQL Workbench, or the command line. I used phpMyAdmin.
  
  -Name the database flask_users.
  
  -Create tables: Run the following SQL queries to create the required tables:
  
    CREATE TABLE tbl_users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE tbl_products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        image VARCHAR(255) DEFAULT NULL
    );

    CREATE TABLE tbl_shopppingcart (
        cart_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES tbl_users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES tbl_products(product_id) ON DELETE CASCADE
    );

    CREATE TABLE tbl_orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        name VARCHAR(100) NOT NULL,
        address TEXT NOT NULL,
        payment_method VARCHAR(50) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES tbl_users(user_id) ON DELETE CASCADE
    );

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Set up the following values in config.py:__

SECRET_KEY=your_secret_key
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=flask_users

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Setup Instructions

__Requisites__

-Python 3.7+

-MySQL database

-Virtual environment tools (venv)

__Steps__

1.Clone the repository:
  
    git clone https://github.com/your-repo/advanced-coding-final-project.git
    cd advanced-coding-final-project
 
2.Set up a virtual environment:

    windows:
      python -m venv env
      env\Scripts\activate        
    macOS/Linux: 
      source env/bin/activate
  
3.Install dependencies:

    pip install -r requirements.txt
  
4.Set up the database:

    Follow the Database Setup section.
  
5.Run the app:

    python run.py

6.Access the application:
       
    Open your browser and go to http://127.0.0.1:5000.

## Screenshots

Home page 

![image](https://github.com/user-attachments/assets/a204f06b-fbe7-48a0-8f3f-9b10f32c31f1)

Products

![image](https://github.com/user-attachments/assets/572e0f5a-b362-4f73-a138-e5e73cf96c2f)

Shopping cart

![image](https://github.com/user-attachments/assets/a40868ba-2ec5-4ae7-b2d1-7e2f7d2d6f1d)




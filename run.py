from app import create_app  # Import the factory function to create the Flask application instance.

# Create an instance of the Flask application
app = create_app()

if __name__ == '__main__':
    """
    Entry point for running the Flask application.

    Runs the application in debug mode, allowing for live reloading and better error messages.
    """
    app.run(debug=True)


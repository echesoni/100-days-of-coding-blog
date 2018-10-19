from flaskblog import app
# when you're working with packages, this will import from __init__.py

# this conditional is only true if we run this script directly (with python)
if __name__ == '__main__':
    app.run(debug=True)

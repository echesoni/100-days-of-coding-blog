from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create app variable and set to instance of Flask
app = Flask(__name__) # __name__ is a special variable in python; it is the name of the module
# if we run script with python directly, __name__ can be = to __main__
app.config['SECRET_KEY'] = '7a72f8e473b3869718d30681ffd7f671'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # slashes are a relative path from current folder
db = SQLAlchemy(app)

# needs to be at bottom to escape circular imports
from flaskblog import routes

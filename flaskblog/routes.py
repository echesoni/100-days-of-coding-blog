from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Jim Halpert',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 9, 2018'
    },
    {
        'author': 'Pam Beasly Halpert',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 10, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    # use flash message to send a one time alert
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')  # pass in category (bs class of success)
        return redirect(url_for('home')) # home is name of function for route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

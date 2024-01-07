from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0400503ac7823818f689b2f033f19bd1'
posts=[
    {
        'author':'Gayathri Ramesh',
        'title':'Backend Development with Flask',
        'content':'First Post',
        'date_posted': 'April 18, 2020'
    },
    {
        'author':'Ashwin Raj',
        'title':'Machine Learning for Dummies',
        'content':'Second Post',
        'date_posted':'August 03, 2020'
    },
    {
        'author':'Dipu Sreedhar',
        'title':'Demystifying the Full Stack',
        'content':'Second Post',
        'date_posted':'December 05, 2020'
        },
        {
        'author':'Sandra Ann Alex',
        'title':'Root Canal the right way',
        'content':'Third Post',
        'date_posted':'September 13, 2020'
        }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form =LoginForm()
    return render_template('login.html', title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)

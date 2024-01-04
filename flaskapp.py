from flask import Flask, render_template

app = Flask(__name__)
posts=[
    {
        'author':'Gayathri Ramesh',
        'title':'Poetry',
        'content':'First Post',
        'date_posted': 'April 18, 2020'
    },
    {
        'author':'Ashwin raj',
        'title':'Machine Learning',
        'content':'Second Post',
        'date_posted':'April 21, 2020'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
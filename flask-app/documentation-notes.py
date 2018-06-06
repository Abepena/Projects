from flask import Flask, url_for, Request

app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return 'This is the index page'

@app.route('/hello')
def hello():
    return 'Hello!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show subpath after path
    return f'Subpath {subpath}'

with app.test_request_context():
    """
    Tests urls with contexts passed in and prints to the console
    """
    print(url_for('index'))
    print(url_for('show_user_profile', username='Abepena'))
    print(url_for('show_post', post_id=1))
    print(url_for('show_subpath',subpath='abe'))

# HTTP METHODS
"""
By default, a route only answers to GET requests
you can use a methods argument of the route() decorator
to handle different HTTP methods
"""

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form
    return render_template('expression')




if __name__ == '(__main__)':
    app.run()

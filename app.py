from flask import Flask
from flask import url_for

app = Flask(__name__)

from markupsafe import escape


@app.route('/')
def hello():
    return 'hello'


@app.route('/user/<name>')
def user_page(name):
    return 'User:{}'.format(escape(name))


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='mzm'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

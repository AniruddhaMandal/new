from flask import Flask
from flask import request
from flask_script import Manager

app = Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World,\n Your Browser is %s</h1>' %user_agent

@app.route('/user/<name>')
def user(name):
    return ('<h1>Hello, %s!</h1>' %name)
    

manager = Manager(app)
if  __name__ == '__main__':
    manager.run()
    app.run(debug = True)
    
    
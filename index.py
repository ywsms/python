__author__ = 'ywsms'
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('index.html',name='name')
'''
@app.route('/username',method=['POST','GET'])
def user():
    if method=='GET':
        return 'hello get'
'''

if __name__ == '__main__':
    app.run()

__author__ = 'ywsms'
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('index.html',name='name')

@app.route('/username',methods=['POST','GET'])
def user():

    return 'hello get'
    print 'test1'
    if request.methods=='GET':
        print 'test2'
        return request.form['username']+'GET'


if __name__ == '__main__':
    app.run(debug=True)


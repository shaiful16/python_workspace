from flask import Flask,request,json


app=Flask(__name__)


@app.route('/')
def index():
    return 'it is index ' + 'method used %s ' % request.method

@app.route('/hello/<userName>')
def userShow(userName):
    return 'hello %s ...' % userName

@app.route('/get/<int:id>')
def getExample(id):
    return 'id is %s ...' % id

@app.route('/post', methods =['POST'])
def postExample():
    return 'method is %s ...' % request.method

@app.route('/<command>')
def command(command):
    if (command == "up"):
        print ("u said up")
        return 'command is ...%s' % command
    elif (command == "down"):
        print("u said up")
        return 'command is ...%s' % command

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(host="192.168.0.100",port=5000)
    #app.run(debug=True, host='0.0.0.0',port=80)  # http://localhost



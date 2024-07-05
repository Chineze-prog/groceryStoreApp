from flask import Flask, request, jsonify

#in any web backend there has to be a server, and we are using python flask as a micro-framework for the web server
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World!'


#start a flask application, which is started on port 5000 on the local computer
if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management System.")
    app.run(port=5000)


"""
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'


#start a flask application, which is started on port 5000 on the local computer
if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management System.")
    app.run(port=5000)
"""

from movement import Movement
from flask import Flask

print('server init!')
ctrl = Movement()
app = Flask(__name__)

@app.route('/stop/')
def stop():
    ctrl.stop()

    return None

@app.route('/forward/')
def forward():
    ctrl.forward()

    return None
@app.route('/rightForward/')
def rightForward():
    ctrl.rightForward()

    return None

@app.route('/leftForward/')
def leftForward():
    ctrl.leftForward

    return None
@app.route('/backward/')
def backward():
    ctrl.backward

    return None

@app.route('/leftBackward/')
def leftBackward():
    ctrl.leftBackward

    return None

@app.route('/rightBackward/')
def rightBackward():
    ctrl.rightBackward()

    return None

@app.route('/rightRotate/')
def rightRotate():
    ctrl.rightRotate()

    return None

@app.route('/leftRotate/')
def leftRotate():
    ctrl.leftRotate()

    return None



if __name__ == 'main':
    app.run(host= '0.0.0.0',port = 5000)
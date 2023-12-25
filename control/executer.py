# -*- coding: utf-8 -*-

from movement import Movement
from flask import Flask

print('server init!')
ctrl = Movement()
app = Flask(__name__)

@app.route('/stop/')
def stop():
    ctrl.stop()

    return 's'

@app.route('/forward/')
def forward():
    ctrl.forward()

    return 'f'
@app.route('/rightForward/')
def rightForward():
    ctrl.rightForward()

    return 'rB'

@app.route('/leftForward/')
def leftForward():
    ctrl.leftForward

    return 'lF'
@app.route('/backward/')
def backward():
    ctrl.backward

    return 'b'

@app.route('/leftBackward/')
def leftBackward():
    ctrl.leftBackward

    return 'lB'

@app.route('/rightBackward/')
def rightBackward():
    ctrl.rightBackward()

    return 'rB'

@app.route('/rightRotate/')
def rightRotate():
    ctrl.rightRotate()

    return 'rR'

@app.route('/leftRotate/')
def leftRotate():
    ctrl.leftRotate()

    return 'lR'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
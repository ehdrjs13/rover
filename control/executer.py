# -*- coding: utf-8 -*-

from movement import Movement
from flask import Flask

print('server init!')
ctrl = Movement()
app = Flask(__name__)

@app.route('/stop/')
def stop():
    ctrl.stop()

    print('stop')

    return 's'

@app.route('/forward/')
def forward():
    ctrl.forward()

    print('forward')

    return 'f'
@app.route('/rightForward/')
def rightForward():
    ctrl.rightForward()

    print('rightforward')

    return 'rB'

@app.route('/leftForward/')
def leftForward():
    ctrl.leftForward

    print('leftForward')

    return 'lF'
@app.route('/backward/')
def backward():
    ctrl.backward

    print('backward')

    return 'b'

@app.route('/leftBackward/')
def leftBackward():
    ctrl.leftBackward

    print('leftbackward')

    return 'lB'

@app.route('/rightBackward/')
def rightBackward():
    ctrl.rightBackward()

    print('rightBackward')

    return 'rB'

@app.route('/rightRotate/')
def rightRotate():
    ctrl.rightRotate()

    print('rightRotate')

    return 'rR'

@app.route('/leftRotate/')
def leftRotate():
    ctrl.leftRotate()

    print('leftRotate')

    return 'lR'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
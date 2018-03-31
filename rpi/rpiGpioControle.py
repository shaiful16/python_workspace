#!flask/bin/python3

from flask import json,jsonify
from flask import Flask, url_for, request
import RPi.GPIO as GPIO # always needed with RPi.GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(25, GPIO.OUT)  # set GPIO 25 as an output. You can use any GPIO port

@app.route('/')
def api_root():
    return 'Welcome'


#http://127.0.0.1:5000/armControlL1?L1pwm=5&L1fb=+1
@app.route('/armControlL1', methods = ['GET'])
def armControlL1():
    p = GPIO.PWM(25, 50)  # create an object p for PWM on port 25 at 50 Hertz

    p.start(50)  # start the PWM on 50 percent duty cycle
    p.ChangeDutyCycle(90)  # change the duty cycle to 90%
    # p.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)
    p.stop()  # stop the PWM output
    # GPIO.cleanup()  # when your program exits, tidy up after yourself

    args = request.args
    L1pwm = args.get('L1pwm')
    print(L1pwm)
    L1fb = args.get('L1fb')
    print(L1fb)
    return 'success'


# http://127.0.0.1:5000/armControlL2?L2pwm=5&L2fb=+1
@app.route('/armControlL2', methods=['GET'])
def armControlL2():
    args = request.args
    L2pwm = args.get('L2pwm')
    print(L2pwm)
    L2fb = args.get('L2fb')
    print(L2fb)
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,)

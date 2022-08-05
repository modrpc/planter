from Adafruit_MotorHAT import Adafruit_MotorHAT 
from Adafruit_MotorHAT import Adafruit_DCMotor
import atexit
import time
import asyncio

import modpy

initdone = False

@modpy.initial
def init():
    global mh, m0, m1, initdone
    if (initdone == False):
        mh = Adafruit_MotorHAT(addr=0x60)
        m0 = mh.getMotor(2)
        m1 = mh.getMotor(3)
        initdone = True

@modpy.func
def go():
    init()
    stop()
    m0.run(Adafruit_MotorHAT.FORWARD)
    m1.run(Adafruit_MotorHAT.FORWARD)
    for i in range(100):
        m0.setSpeed(i)
        m1.setSpeed(i)
        time.sleep(0.05)

@modpy.func
def right():
    init()
    stop()
    m0.run(Adafruit_MotorHAT.FORWARD)
    for i in range(100):
        m0.setSpeed(i)
        time.sleep(0.05)

@modpy.func
def left():
    init()
    stop()
    m1.run(Adafruit_MotorHAT.BACKWARD)
    for i in range(100):
        m1.setSpeed(i)
        time.sleep(0.05)

@modpy.func
def back():
    init()
    stop()
    m0.run(Adafruit_MotorHAT.BACKWARD)
    m1.run(Adafruit_MotorHAT.BACKWARD)
    for i in range(100):
        m0.setSpeed(i)
        m1.setSpeed(i)
        time.sleep(0.05)

@modpy.func
def stop():
    global m0, m1
    init()
    m0.run(Adafruit_MotorHAT.RELEASE)
    m1.run(Adafruit_MotorHAT.RELEASE)

@modpy.final
def final():
    stop()

#atexit.register(stop)


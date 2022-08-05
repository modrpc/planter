from __future__ import division
import time
import Adafruit_PCA9685

import asyncio

import modpy

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


@modpy.initial
def init():
    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

@modpy.func
def up():
    pwm.set_pwm(4, 0, servo_min)
    time.sleep(1)

@modpy.func
def down():
    pwm.set_pwm(4, 0, servo_max)
    time.sleep(1)

@modpy.func
def rotate_right():
    pwm.set_pwm(8, 0, servo_min)
    time.sleep(1)
    
@modpy.func
def rotate_left():
    pwm.set_pwm(8, 0, servo_max)
    time.sleep(1)

import RPi.GPIO as GPIO

class BiColourLed(object):

    def __init__(self, red_pin, green_pin):
        self.red_pin = red_pin
        self.green_pin = green_pin
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(red_pin, GPIO.OUT)
	GPIO.setup(green_pin, GPIO.OUT)

    def off(self):
	GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, False)	
	
    def red(self):
	GPIO.output(self.red_pin, True)
        GPIO.output(self.green_pin, False) 

    def green(self):
	GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, True) 

    def yellow(self):
	GPIO.output(self.red_pin, True)
        GPIO.output(self.green_pin, True) 

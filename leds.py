
class BiColourLed(object):

    def __init__(self, red_pin=None, green_pin=None):
        self.red_pin = red_pin
        self.green_pin = green_pin

    @property
    def off(self):
        print "OFF"

    def red(self):
        print "RED"

    def green(self):
        print "GREEN"

    def yellow(self):
        print "YELLOW"
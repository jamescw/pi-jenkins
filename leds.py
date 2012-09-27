import RPi.GPIO as GPIO

class BiColourLed(object):
    def __init__(self, red_pin, green_pin):
        self.colours = {
            'off': False,
            'red': False,
            'green': False,
        }
        self.red_pin = red_pin
        self.green_pin = green_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)

    def _set_colour(self, colour, value=None):
        if colour in self.colours:
            if value:
                for k,v in self.colours.items():
                    if v is colour:
                        self.colours[k] = True
                    else:
                        self.colours[k] = False
                GPIO.output(self.red_pin, self.colours['red'])
                GPIO.output(self.green_pin, self.colours['green'])
            return self.colours[colour]
        else:
            raise KeyError("This LED does not support colour {0}".format(colour))

    def __getattr__(self, colour):
        return self._set_colour(colour)

    def __setattr__(self, colour, value):
        return self._set_colour(colour, value)

    def __repr__(self):
        return "LED is state is: ".format(self.colours)


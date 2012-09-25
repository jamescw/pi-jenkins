import time

from jenkins import Jenkins

from leds import BiColourLed

JENKINS_URL = "http://jenkins.uktv.rethought-solutions.com/"

LEDS = [
    BiColourLed(),
    BiColourLed()
]

JOBS = [
    {
        'name': 'ukcms-widget_refresh',
        'led': LEDS[0]
    },
    {
        'name': 'ukcms-develop',
        'led': LEDS[1]
    }
]

def poll():
    jenkins = Jenkins(JENKINS_URL)
    while True:
        remote_jobs = jenkins.get_jobs()
        for remote in remote_jobs:
            for local in JOBS:
                if local['name'] == remote['name']:
                    led = local['led']
                    if remote['color'] == 'blue':
                        led.green()
                    elif remote['color'] == 'red':
                        led.red()
                    else:
                        if led.yellow:
                            led.off()
                        else:
                            led.yellow()
        time.sleep(1)


if __name__ == "__main__":
    try:
        poll()
    except KeyboardInterrupt:
        pass




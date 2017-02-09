# wiringPi fpr Python has to be installed to run this code (manual build): https://github.com/WiringPi/WiringPi-Python
# for Pi Zero: reroute the GPIOS following the tutorial on adafruit (https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio)
# for Pi Zero: you have to rewire the GPIOS with the following command after booting: gpio_alt -p 18 -f 5

from flask import Flask, request
import requests

import sys

# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period_in = 0.015
delay_period_out = 0.02
delay_break = 1 


app = Flask(__name__)
 
ACCESS_TOKEN = "TO DO: get it from your facebook app!"
 
 
def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
   # print(resp.content)
    print data 
    #matching = [s for s in data if "text" in s]
    #print matching
    for s in data.items():
	print s[1]
   # nu_data = str(data[1])
    #print nu_data
   # if nu_data == "{'text': u'hug'}":
#		print "hug me now"

    st=""
    for key,val in data.iteritems():
     	st = st + key + str(val)
    print st
    if "L-O-V-E" in st:
	print "hug me"
        # server and servo listen                                                
    	for pulse in range(50, 150, 1):
      		wiringpi.pwmWrite(18, pulse)
      		time.sleep(delay_period_in * 60 / 100)
    	for pulse in range(150, 50, -1):
      		wiringpi.pwmWrite(18, pulse)
      		time.sleep(delay_period_out * 60 / 100)
    	time.sleep(delay_break * 60 / 100)

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']
 
@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    if "hugs" in str(message):
    	reply (sender, "Thx for spreading the L-O-V-E, you're awesome!")  
    else:
	reply(sender, "%s? let me think ... nope :)!" % (message))
    #print data 
    return "ok"
   
 
if __name__ == '__main__':
    app.run(debug=True)
   

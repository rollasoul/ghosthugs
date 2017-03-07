# get fb-hugs on 8266 module, control servo movement
# run with fb_hugs_server.py (server), ngrok (server), hugs_letter_server.py (server) + Facebook Page incl. app and webhook

import socket
import time
import machine  
s = socket.socket()
host = "147.75.197.237"
port = 12344
while True:
    try:
        while True:
            s = socket.socket()
            s.connect((host, port))
            time.sleep(1)
            s.send("ready")
            output = s.recv(2048)
            if "hug" in output:
                p12 = machine.Pin(12)
                pwm12 = machine.PWM(p12)
                servo = machine.PWM(machine.Pin(12), freq=50)
                servo.duty(44)
                time.sleep(1)
                servo.duty(115)
            s.close()
    except:
        pass

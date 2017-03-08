# for use with 4 servos, simulating arm movement: open arms and wait for fingers, after 5s close arms for hug

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
                p14 = machine.Pin(14)
                pwm14 = machine.PWM(p14)
                servo1 = machine.PWM(machine.Pin(14), freq=50)
                servo1.duty(80)
                time.sleep(5)
                p12 = machine.Pin(12)
                pwm12 = machine.PWM(p12)
                servo = machine.PWM(machine.Pin(12), freq=50)
                servo.duty(44)
                time.sleep(1)
                servo.duty(80)
                servo1.duty(44)
            s.close()
    except:
        pass

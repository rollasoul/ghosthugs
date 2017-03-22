import socket
import time
import machine  
s = socket.socket()
host = "TO DO: Enter ip-address of remote server"
port = 12344
counter = 0
while True:
    try:
        while True:
            s = socket.socket()
            s.connect((host, port))
            time.sleep(1)
            s.send("ready")
            output = s.recv(2048)
            print(output)
            if "disconnect" in output:
                s.close()
                if counter == 1:
                    if "High five" in output:
                        p13 = machine.Pin(13)
                        pwm13 = machine.PWM(p13)
                        servo_s = machine.PWM(machine.Pin(13), freq=50)
                        servo_s.duty(130)
                        time.sleep(3)
                        servo_s.duty(120)
                        time.sleep(1)
                        servo_s.duty(34)
                        counter = 0
                else:
                    counter = 1
    except:
        pass

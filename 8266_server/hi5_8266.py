import socket
import time
import machine  
s = socket.socket()
host = "147.75.197.237"
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
                    if "hi sis" in output:
                        p13 = machine.Pin(13)
                        pwm13 = machine.PWM(p13)
                        servo_s = machine.PWM(machine.Pin(13), freq=50)
                        p14 = machine.Pin(14)
                        pwm14 = machine.PWM(p14)
                        servo_b = machine.PWM(machine.Pin(14), freq=50)
                        p12 = machine.Pin(12)
                        pwm12 = machine.PWM(p12)
                        servo_a = machine.PWM(machine.Pin(12), freq=50)
                    #hi
                        servo_s.duty(30)
                        servo_b.duty(60)
                        servo_a.duty(100)
                        time.sleep(3)
                        servo_s.duty(50)
                        servo_a.duty(60)
                        servo_b.duty(50)
                        time.sleep(2)
                        servo_s.duty(70)
                        servo_a.duty(80)
                        servo_b.duty(30)
                        time.sleep(1)
                        counter = 0
                    elif "High five" in output:
                        p13 = machine.Pin(13)
                        pwm13 = machine.PWM(p13)
                        servo_s = machine.PWM(machine.Pin(13), freq=50)
                        p14 = machine.Pin(14)
                        pwm14 = machine.PWM(p14)
                        servo_b = machine.PWM(machine.Pin(14), freq=50)
                        p12 = machine.Pin(12)
                        pwm12 = machine.PWM(p12)
                        servo_a = machine.PWM(machine.Pin(12), freq=50)
                        servo_s.duty(30)
                        servo_b.duty(60)
                        servo_a.duty(100)
                        time.sleep(3)
                        servo_s.duty(50)
                        servo_a.duty(80)
                        servo_b.duty(60)
                        time.sleep(2)
                        servo_s.duty(70)
                        servo_a.duty(80)
                        servo_b.duty(30)
                        time.sleep(1)
                        counter = 0
                else:
                    counter = 1
    except:
        pass

import socket
import time
import machine  
led1 = machine.Pin(5, machine.Pin.OUT)
led2 = machine.Pin(4, machine.Pin.OUT)
adc = machine.ADC(0) 
s = socket.socket()
host = "To Do: Enter ip-address of remote server"
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
                        if adc.read() > 200:
                            for i in range(3):
                                led1.high()
                                time.sleep(0.1)
                                led1.low()
                                time.sleep(0.1)
                                led2.high()
                                time.sleep(0.1)
                                led2.low()
                                time.sleep(0.3)
                        else:
                            led1.high()
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

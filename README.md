# ghosthugs

Send real "hugs" - via fb messenger.
- follow the instructions on this tutorial(http://masnun.com/2016/05/22/building-a-facebook-messenger-bot-with-python.html) to set up a facebook bot, a flask server (handles fb messenger api) and ngrok (handles https and opens local server to internet - potential security risk)
- if you are running this on remote server and 8266 module: use files in 8266_server folder (and ignore the below)
- if you are running this on the pi zero: wiringPi fpr Python has to be installed to run this code (manual build) https://github.com/WiringPi/WiringPi-Python, then reroute the GPIOS following the tutorial on adafruit (https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio) and you have to rewire the GPIOS with the following command after booting: gpio_alt -p 18 -f 5
- run hugbott.py in connection with ngrok (and update https address in fb app webhook).
```
./ngrok http 5000
```
```
sudo python /ghosthugs/hugbott.py
```
Connect a servo to it and control with fb-messages from anywhere - by default triggered by text message "hugs". 

(this is just a very quick readme that needs a lot more work on it)

# ghosthugs

Send real "hugs" - via fb messenger. 

- follow the instructions on this tutorial(http://masnun.com/2016/05/22/building-a-facebook-messenger-bot-with-python.html) to set up a facebook app, a flask server on the pi in connection with python.
- run hugbott.py in connection with ngrok (and update https address in fb app webhook).
```
./ngrok http 5000
```
```
sudo python /ghosthugs/hugbott.py
```
Connect a servo to it and control with fb-messages from anywhere - by default triggered by text message "hugs". 

(this is just a very quick readme that needs a lot more work on it)

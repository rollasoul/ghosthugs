# sets up flask-server that gets hugs from fb messenger app via page/webhooks
# run with hugs_letter_server.py (server), ngrok (server), 8266_hugs.py (8266) + Facebook Page incl. app and webhook

# server script for flask server

from flask import Flask, request
import requests
from __future__ import print_function
import sys
# Server

app = Flask(__name__)

ACCESS_TOKEN = "TO DO: Get access token from fb page"

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
#   print "hug me now"
    	st=""
    	for key,val in data.iteritems():
    		st = st + key + str(val)
    	print st
    	if "L-O-V-E" in st:
    		print "hug me"
            f = open('hug.txt', 'w')
            f.write('hug me\n')
            f.close() 

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

@app.route('/', methods=['POST'])
def handle_incoming_messages():
	data = request.json
    	inbound_check = data['entry'][0]['messaging'][0]['timestamp']
	print "check is  %d" % (inbound_check)
	if inbound_check > 0:
		sender = data['entry'][0]['messaging'][0]['sender']['id']
    		message = data['entry'][0]['messaging'][0]['message']['text']
    		if "hugs" in str(message):
    			reply(sender, "Thx for spreading the L-O-V-E, you're awesome!")
    		else:
  			reply(sender, "%s? let me think ... nope :)!" % (message))

		return "ok"
	else:
		return "200"

if __name__ == '__main__':
		app.run(debug=True)

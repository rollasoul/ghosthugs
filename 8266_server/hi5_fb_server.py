# server script for flask server

from flask import Flask, request
import requests
import sys
# Server

app = Flask(__name__)

ACCESS_TOKEN = "TO DO: Get access token from Facebook messenger API"

def reply(user_id, msg):
    	data = {
        	"recipient": {"id": user_id},
        	"message": {"text": msg}
    	}
    	resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
   	# print(resp.content)
    	print "data out is %s" %(data)
    	#matching = [s for s in data if "text" in s]
    	#print matching
    	#for s in data.items():
    		#print s[1]
   # nu_data = str(data[1])
    #print nu_data
   # if nu_data == "{'text': u'hug'}":
#   print "hug me now"
    	st=""
    	for key,val in data.iteritems():
    		st = st + key + str(val)
    	#print st
    	if "ez" in st:
    	    print "hi sis"
            f = open('hug.txt', 'w')
            f.write('hi sis\n')
            f.close()
        if "yesssssss" in st:
            print "High five"
            f = open('hug.txt', 'w')
            f.write('High five\n')
            f.close()

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

@app.route('/', methods=['POST'])
def handle_incoming_messages():
	data = request.json
	print "data-in is  %s" % (data)
	sender = data['entry'][0]['messaging'][0]['sender']['id']
    	message = data['entry'][0]['messaging'][0]['message']['text']
    	if "Hi sis" in str(message):
    			reply(sender, "ez ...")
        elif "Hi bro" in str(message):
      		        reply(sender, "ez ...")
        elif "High five" in str(message):
        	        reply(sender, "yesssssss ...")
        if str(message) not in ("Hi sis", "Hi bro", "High five"):
  			reply(sender, "%s? let me think ... nope :)!" % (message))

	return "ok"
	return "200"

if __name__ == '__main__':
		app.run(debug=True)



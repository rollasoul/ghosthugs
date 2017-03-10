# server script for flask server

from flask import Flask, request
import requests
import sys
# Server

app = Flask(__name__)

ACCESS_TOKEN = "EAAQ1bSZB1vUsBAJBEha6KOzRumpsVi9CgulwOcFTom3rSJQ8dQdJSqFwPAj1Gb7wtWKEZBd4k0dyyuJNSOOyicv3GgxafMjkUyYh7AAhhIh2lXj5ZC7YeCHQ9uGlN2ok3WJ0pMEjcafA2ROX1B2cwIiQ9VkuqdMcr7xtuXLYwZDZD"

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
    	inbound_check = data['entry'][0]['messaging'][0]['timestamp']
	print "check is  %d" % (inbound_check)
	if inbound_check > 0:
		sender = data['entry'][0]['messaging'][0]['sender']['id']
    		message = data['entry'][0]['messaging'][0]['message']['text']
    		if "Hi sis" in str(message):
    			reply(sender, "ez ...")
                if "Hi bro" in str(message):
      		        reply(sender, "ez ...")
                if "High five" in str(message):
        	        reply(sender, "yesssssss ...")
    		else:
  			reply(sender, "%s? let me think ... nope :)!" % (message))

		return "ok"
	else:
		return "200"

if __name__ == '__main__':
		app.run(debug=True)



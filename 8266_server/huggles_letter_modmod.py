# remote server running ubuntu 16.04

# Server
import socket
import sys
import time

# server setup
host = '0.0.0.0'
port_pi = 12344
address_pi = (host, port_pi)

server_socket_pi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_pi.bind(address_pi)
server_socket_pi.listen(5)
# server and servo listen
while True:
		with open('hug.txt', 'r') as myfile:
	    			text=myfile.read().replace('\n', '')
	    			if "hi sis" in text:
					myfile = open('hug.txt', 'w')
					myfile.write('')
					myfile.close
					msg = "hi sis.disconnect"
					conn_pi, address_pi = server_socket_pi.accept()
					print "Connected to pi at ", address_pi
					if conn_pi.recv(2048) == "ready":
			    			conn_pi.send(msg)
			    			print "Disconnecting from pi"
			            		conn_pi.close()
			            		print "waiting for highs ... "
	    			elif "High five" in text:
					myfile = open('hug.txt', 'w')
                        		myfile.write('')
                        		myfile.close()
					text = "High five.disconnect"
					conn_pi, address_pi = server_socket_pi.accept()
					print "Connected to pi at ", address_pi
					if conn_pi.recv(2048) == "ready":
		    				conn_pi.send(text)
		    				print "Disconnecting from pi"
		            			conn_pi.close()
		            			print "waiting for highs ... "

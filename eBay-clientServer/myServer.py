#!/usr/bin/env python
import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

#Create custom HTTPRequestHandler class
class myHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()

	def processPath(self, command):
        if path == 'getSellerRequest':
			self.send_response(200)
	        self.wfile.write('<br>Path: %s' % path)
	        self.wfile.write('<br>Query: %s' % qs)
	        self.wfile.write('<br>Seller Name: %s' % qs['SELLER_NAME'][0])

			#send file content to client
			self.wfile.write("<html><head><title>My Response</title></head>")
			self.wfile.write("<body><h1>I Got your request!!</h1>")
			self.wfile.write("</body></html>")

	#handle GET command
	def do_GET(self):		
		#send header first
		self.send_header('Content-type','text-html')
		self.end_headers()
		#localhost:8000/getSellerRequest?sellerName=hisName;someOtherInfo=otherInfo

		validCommands = ['getSellerRequest']


        import urlparse
        qs = {}
        path = self.path
        if '?' in path:
            path, tmp = path.split('?', 1)
            qs = urlparse.parse_qs(tmp)
        if path in validCommands:
        	self.processPath(path)
        else:
			self.send_response(400)

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), myHTTPRequestHandler)

	try:
		httpd.serve_forever()

	except KeyboardInterrupt:
		pass
	httpd.server_close()
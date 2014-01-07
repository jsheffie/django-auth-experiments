import requests
from requests.auth import HTTPBasicAuth
# also: HTTPProxyAuth, HTTPDigestAuth
from requests.exceptions import RequestException, ConnectionError, HTTPError, URLRequired, TooManyRedirects
import json
import sys

def set_port(port=None):
	""" This helper function gives the user the ability to set or not set the port"""
	if port:
		port = ":" + str(port)
	else:
		port=""
	return port

def server_request(sreq, server_url, auth=None, show_headers=None):

	req=None
	try:
		req = sreq.get(server_url, auth=auth)
		if show_headers:
			print "---------- Sent Headers ---------->>>>>>>>"
			print json.dumps(dict(sreq.headers), indent=4)

	except ConnectionError:
		print "ERROR: Could not connect to server: %s" % ( server ) 
		print "       Is the server down?"
		raise
	except RequestException:
		print "ERROR: [%s] There was an ambiguous exception that occurred while handling your request." % ( server )
		raise
	except HTTPError:
		print "ERROR: [%s] An HTTP error occured." % ( server )
		raise
	except URLRequired:
		print "ERROR: [%s] A valid URL is required to make a request." % ( server )
		results_list.append( "{0:25s}".format(server) + "ERROR Processing")
		raise
	except TooManyRedirects:
		print "ERROR: [%s] Too many redirects." % ( server )
		raise
	except:
		print "ERROR: Processing: [%s]" % ( server ) 
		raise

	if show_headers:
		print "<<<<<<<<<---------- Received Headers ----------"
		print json.dumps(dict(req.request.headers), indent=4)
		print json.dumps(dict(req.headers), indent=4)
		print "-"*50
	return req

if __name__ == '__main__':

	show_http_headers=True
	server = 'localhost'
	server_protocol='http://'
	username='admin'
	password='password'
	basic_auth = HTTPBasicAuth(username, password)
	port = 8000

#	urls = [ "/users/", "/groups/", "/users/1/" ]
	urls = [ "/users/"]

	port = set_port( port )
	sreq = requests.Session()

	for url in urls:
		server_url = server_protocol + server + port + url
		print "============> " + "{0:35s}".format(server_url) + " <============"

		req = server_request(sreq, server_url, show_headers=show_http_headers)

		if req.status_code != 200:
			print "Warning: status code %d" % req.status_code
			print "         retry with authentication"
			#import pdb; pdb.set_trace()
			req = server_request(sreq, server_url, auth=basic_auth, show_headers=show_http_headers)

		if req.status_code != 200:
			print "ERROR: status code %d" % req.status_code
			sys.exit(1)

		print json.dumps(dict(req.json()), indent=4)

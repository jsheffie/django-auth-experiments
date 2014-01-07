import requests
from requests.auth import HTTPBasicAuth
# also: HTTPProxyAuth, HTTPDigestAuth
from requests.exceptions import RequestException, ConnectionError, HTTPError, URLRequired, TooManyRedirects
import json
import sys

def make_url( http_prefix, server, port, uri ):
	# TODO: make a bit smarter about slashes.
    if port:
        url = "%s://%s:%d%s" % ( http_prefix, server, port, uri )
    else:
        url = '%s://%s%s' % ( http_prefix, server, uri )
        
    return url

if __name__ == '__main__':

	# make a request to http://localhost:8000/auth/view/
	# sould give me a 302 to login.
	# --> http://localhost:8000/accounts/login/?next=/auth/view/
	# here we want to store off the csrftoken
	# then go to http://localhost:8000/auth/view/ with a session.

	server = 'localhost'
	server_protocol='http'
	username='admin'
	password='password'
	basic_auth = HTTPBasicAuth(username, password)
	port = 8000
	
	client = requests.Session()

	view_url = make_url( server_protocol, server, port, '/auth/view/')
	login_url = make_url( server_protocol, server, port, '/accounts/login/?next=/auth/view/')

	client.get( view_url )

	csrftoken = client.cookies['csrftoken']

	# 403
	# without the csrfmiddleware in the login_data this will return a 403
	#
	# login_data = dict(username=username, password=password)
	# resp = client.post(login_url, data=login_data, headers={"Referer": "/auth/view/" })

	# 200
	login_data = dict(username=username, password=password, csrfmiddlewaretoken=csrftoken)
	#resp = client.post(login_url, data=login_data, headers={"Referer": "/auth/view/" })
	resp = client.post(login_url, data=login_data )

	if False:
		print "---------- Sent Headers ---------->>>>>>>>"
		print json.dumps(dict(client.headers), indent=4)
		print "<<<<<<<<<---------- Received Headers ----------"
		print json.dumps(dict(resp.request.headers), indent=4)
		print json.dumps(dict(resp.headers), indent=4)
		print "-"*50
	print resp.text

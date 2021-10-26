# Python 3 server
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import requests

hostName = ''
serverPort = 2000

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        
        if post_body:
            request = json.loads(post_body)
            print('Incomming payload:', request)
            
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            payload = request['number'] * 2
            
            print('Payload to sent:', payload)
            # response = requests.post('http://127.0.0.1:3000', headers=headers, json=payload)
            
        
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
with HTTPServer((hostName, serverPort), handler) as server:
    server.serve_forever()
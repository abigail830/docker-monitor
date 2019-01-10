from dockermon.SimpleHTTPRequestHandler import SimpleHTTPRequestHandler
from http.server import HTTPServer

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8099), SimpleHTTPRequestHandler)
    httpd.serve_forever()


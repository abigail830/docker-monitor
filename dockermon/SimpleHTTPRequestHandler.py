from http.server import BaseHTTPRequestHandler
from dockermon.ContainerInfoCollector import ContainerInfoCollector
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        collect = ContainerInfoCollector()
        print("Going to access docker ...")
        result = collect.collect_info_list()
        json_result = json.dumps([info.__dict__ for info in result])
        print("{}".format(json_result))

        self._set_headers()
        self.wfile.write(json_result)

#!/usr/bin/env python3
import http.server
from functools import partial

class CachelessHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Access-Control-Allow-Origin", "*")
        http.server.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    handler_class = partial(CachelessHTTPRequestHandler, directory="tiles/")
    http.server.test(HandlerClass=handler_class, port=8080, bind="127.0.0.1")

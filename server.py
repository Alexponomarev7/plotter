#! /usr/bin/env python3

import http.server

PORT = 1998

httpd = http.server.HTTPServer(('', PORT), http.server.CGIHTTPRequestHandler)
httpd.serve_forever()

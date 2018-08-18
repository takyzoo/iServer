#!/usr/bin/env python3

import http.server, socketserver, ui, console, iServer

# Read the README.MD first before using this script!

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port ", PORT)
httpd.serve_forever()

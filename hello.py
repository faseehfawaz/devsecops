# hello.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, DevSecOps World!")

# CHANGE 1: Use Port 8080 (Safe for non-root users)
# CHANGE 2: Keep 0.0.0.0 to allow external connections
server = HTTPServer(('0.0.0.0', 8080), SimpleHandler) # nosec
print("Server starting on port 8080...")
server.serve_forever()

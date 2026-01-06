from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # The HTML message
        message = """
        <html>
        <head><title>DevSecOps App</title></head>
        <body style="background-color: #2d2d2d; color: white; font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>Mission Accomplished!</h1>
            <p>Your DevSecOps Pipeline is serving this page live from Azure.</p>
            <p>Built with GitHub Actions, Terraform, and Docker.</p>
        </body>
        </html>
        """
        self.wfile.write(bytes(message, "utf8"))


# Listen on Port 80, Address 0.0.0.0 (All interfaces)
# Add '# nosec' to the end of the line to suppress the Bandit warning
server = HTTPServer(('0.0.0.0', 80), SimpleHandler) # nosec
print("Server starting on port 80...")
server.serve_forever()

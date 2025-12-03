#!/usr/bin/env python3
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler with basic API endpoints."""

    def _send_json(self, data, status=200):
        """Helper method to send JSON data."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_text(self, text, status=200):
        """Helper method to send plain text."""
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def do_GET(self):
        """Handle GET requests and route endpoints."""

        # Root endpoint "/"
        if self.path == "/":
            return self._send_text("Hello, this is a simple API!")

        # /data endpoint returns JSON
        elif self.path == "/data":
            sample = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            return self._send_json(sample)

        # /status endpoint
        elif self.path == "/status":
            return self._send_text("OK")

        # /info endpoint (as shown in Expected Output)
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            return self._send_json(info)

        # Anything else → 404 Not Found
        else:
            self._send_text("Endpoint not found", status=404)


if __name__ == "__main__":
    server_address = ("", 8000)  # Listen on port 8000
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

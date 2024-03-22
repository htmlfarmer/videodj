from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/example_script':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            result_data = {"message": "This is the result of the Python script.", "value": 42}
            self.wfile.write(json.dumps(result_data).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
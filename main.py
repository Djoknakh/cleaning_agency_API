import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import logging
from sms import *

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

        meta_data = json.loads(post_data)
        phone = meta_data["order"]["tel"]
        print(self.headers)
        print(phone)

    # def _set_phone(self):
    #     post_data = self.rfile.read(content_length)
    #     meta_data = json.loads(post_data)
    #     phone = meta_data["order"]["tel"]
    #     print(self.headers)
    #     print(phone)
    #     return phone

if __name__ == "__main__":

    mysms = Sms_ru("+7-999-000-00-99")
    print(mysms.validation_phone())

run(handler_class=HttpGetHandler)

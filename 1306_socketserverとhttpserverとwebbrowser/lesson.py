import http.server
import socketserver


with socketserver.TCPServer(('127.0.0.1', 8000), 
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

# ブラウザから 127.0.0.1:8000をアクセスすれば、フォルダ構成が見える

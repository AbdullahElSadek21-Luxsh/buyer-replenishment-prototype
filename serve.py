"""Replenish LAN server.
- Threaded, so several people on the network can load it at once without blocking.
- No-cache headers, so a plain browser refresh always gets the latest build.
- Prints the current LAN IP on start (handy since DHCP can reassign it)."""
import http.server, socket
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8090

class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"          # keep-alive, but threaded so it's safe
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
    def log_message(self, *args):
        pass

def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)); ip = s.getsockname()[0]; s.close()
        return ip
    except Exception:
        return "127.0.0.1"

srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
srv.daemon_threads = True
print("Replenish is running. Share this on your network:")
print("    http://%s:%d" % (lan_ip(), PORT))
print("Keep this window open. Ctrl+C or close it to stop.")
srv.serve_forever()

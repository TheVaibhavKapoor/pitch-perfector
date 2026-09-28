"""
Smart static file server with .html extension fallback.
Serves files from the current directory on port 3000.
If a URL has no extension and no matching file, tries adding .html.
"""
import http.server
import os
import urllib.parse
PORT = 3001

class SmartHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Decode the URL path
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path)

        # Strip leading slash and get local file path
        local = path.lstrip('/')
        if local == '':
            local = 'index.html'

        # If the file exists as-is, serve it normally
        if os.path.isfile(local):
            return super().do_GET()

        # If no extension and file not found, try adding .html
        _, ext = os.path.splitext(local)
        if not ext:
            candidate = local + '.html'
            if os.path.isfile(candidate):
                # Rewrite the path and serve
                self.path = '/' + candidate + (('?' + parsed.query) if parsed.query else '')
                return super().do_GET()

        # Fall through to default (will 404)
        return super().do_GET()

    def end_headers(self):
        # Disable browser caching so edits show immediately
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"  {self.address_string()} - {format % args}")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with http.server.ThreadingHTTPServer(('', PORT), SmartHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"Serving: {os.getcwd()}")
        print(f"Auto .html extension enabled")
        print(f"Press Ctrl+C to stop\n")
        httpd.serve_forever()

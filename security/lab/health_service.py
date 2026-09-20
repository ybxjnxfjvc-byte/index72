from http.server import BaseHTTPRequestHandler,HTTPServer
import json,os
HOST='127.0.0.1'; PORT=int(os.getenv('PORT','8080'))
def payload(path):
 if path=='/health': return 200,{'ok':True,'service':'portfolio-security-lab'}
 return 404,{'error':'not_found'}
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  code,data=payload(self.path); body=json.dumps(data).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
 def log_message(self,*a): pass
if __name__=='__main__': HTTPServer((HOST,PORT),H).serve_forever()

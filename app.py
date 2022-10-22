# sample-web-app/app.py
from flask import Flask 
from http.server import BaseHTTPRequestHandler

app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to My website!</h1>"
  
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(self.headers.get('x-forwarded-for').encode())
    return

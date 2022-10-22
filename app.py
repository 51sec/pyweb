# sample-web-app/app.py
from flask import Flask, request

app = Flask(__name__) 
  
@app.route("/") 
def home_view():
        return "<h1>Welcome to My PY website!</h1>"
    
def home_view():
        ip_addr = request.remote_addr
        return '<h1> Your IP address is:' + ip_addr +"</BR>"

@app.route('/client')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> Your IP address is:' + ip_addr


@app.route('/client')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Your IP address is:' + ip_addr


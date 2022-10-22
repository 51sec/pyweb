# sample-web-app/app.py
from flask import Flask

app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return '<h1> Your IP address is:' + ip_addr +"</BR>"
        return "<h1>Welcome to My PY website!</h1>"
  

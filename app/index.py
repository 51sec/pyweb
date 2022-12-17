# sample-web-app/app.py
#from flask import Flask 
  
#app = Flask(__name__) 
  
#@app.route("/") 
#def home_view(): 
#        return "<h1>Welcome to My website!</h1>"


from flask import Flask, request

app = Flask(__name__) 
  
@app.route("/") 
def home_view():
  
        ip_addr1 = request.remote_addr
        ip_addr2 = request.environ['REMOTE_ADDR']
        ip_addr3 = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        return "</BR>" +"</BR>" +"</BR>" +"<h1>Welcome to My PY website!</h1>"+"</BR>" + "<h1> Your IP address is:" + ip_addr1 +"</BR>" + "<h1> Your IP address is:" + ip_addr2 + "</BR>" + "<h1> Your IP address is:" + ip_addr3

from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/')
def home():
    return 'The server is up and running\nThis is the homepage'
    

@app.route('/postreceive/', methods = ['POST','GET'])
def postreceive():
    if request.method == 'POST':
        #return str(request.args.get("zen",'NO ZEN'))
        return request.data
    if request.method == 'GET':
        return 'GET Request made\n'+str(request.args.get("zen",'NO ZEN'))
    
    
    
# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

global app_data

@app.route('/')
def home():
    return 'The server is up and running\nThis is the homepage'
    

@app.route('/postreceive/', methods = ['POST','GET'])
def postreceive():
    if request.method == 'POST':
        if validate_postreceive_hook(json.loads(request.data)):
            return 'Invalid Data'
        else:
            return 'OK Fine'
    else:
        return 'Invalid Method-%s'%(request.method)
        
# Loading json data
with open('app_data.json','r') as f:
    app_data = json.load(f)
    
def validate_postreceive_hook(data):
    if data['repository']['html_url'] != app_data['html_url'] :
        return False
    return True

# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
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
        try: 
            validate_postreceive_hook(request.data)
            return "Data Validation : Complete"
        except ValueError,e:
            return str(e)
        return request.data
    else:
        return "Invalid METHOD %s" %str(request.method)
        
# Loading json data
with open('app_data.json','r') as f:
    app_data = json.load(f)
    
def validate_postreceive_hook(data):
    if data['repository']['html_url'] != app_data['html_url'] :
        raise ValueError('Invalid Repository URL')

# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
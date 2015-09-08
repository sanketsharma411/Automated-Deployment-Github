from flask import Flask, request, jsonify
import json
app = Flask(__name__)

GLOBAL app_data

@app.route('/')
def home():
    return 'The server is up and running\nThis is the homepage'
    

@app.route('/postreceive/', methods = ['POST','GET'])
def postreceive():
    if request.method == 'POST':
        try: 
            validate_postreceive_hook(request.data)
        except ValueError,e:
            return str(e)
        return str(request.data.get("zen",'NO ZEN'))
    else:
        return "Invalid METHOD %s" %str(request.method)
        
# Loading json data
with open('app_data.json','r') as f:
    app_data = json.load(f)
    print app_data
    
def validate_postreceive_hook(data):
    if data['html_url'] == app_data['html_url'] :
        return None
    else:
        raise ValueError('Invalid data')
    
# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
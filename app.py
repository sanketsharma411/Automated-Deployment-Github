from flask import Flask, request, jsonify
import json,subprocess
app = Flask(__name__)

######################################################
## Loading Validation Data
######################################################
global app_data
# Loading json data
with open('app_data.json','r') as f:
    app_data = json.load(f)


@app.route('/')
def home():
    return 'The server is up and running\nThis is the homepage'
    

@app.route('/postreceive/', methods = ['POST','GET'])
def postreceive():
    if request.method == 'POST' and validate_postreceive_hook(json.loads(request.data)):
        # Now run the bash_script for updating the local git repo
        run_bash_script()
        return 'Bash Script Running'
        
    
def validate_postreceive_hook(data):
    """Validate the passed dict by comparing it with local data"""
    if data['repository']['html_url'] != app_data['html_url'] :
        return False
    return True

def run_bash_script():
    """Run the defined bash_script"""
    subprocess.call('./git_pull.sh',shell=True)
    
# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
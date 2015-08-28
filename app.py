from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'The server is up and running\nThis is the homepage'
    

# If called from command line run in Flask development server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
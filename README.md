# flask-api-test
Testing automated deplolyment of apps using GitHub's Post-receive hooks



### Done 
1. Create a basic Flask App
2. Serve it through gunicorn on AWS EC2 instance

### Stuff to do

3. Setup a GitHub post-receive hook for this project
4. Accept the POST request in Flask, and look into what it is
5. Use logsol's [Github-Auto-Deploy](https://github.com/logsol/Github-Auto-Deploy) tool or write your own 
to accept a POST request from GitHub and update the local repo.


## Notes:
1. We won't be editing any of the files from the production server.

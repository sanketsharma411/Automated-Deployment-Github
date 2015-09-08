# flask-api-test
Testing automated deplolyment of code using GitHub's Post-receive hooks



### Done 
1. Create a basic Flask App
2. Serve it through gunicorn on AWS EC2 instance
3. Setup a GitHub post-receive hook for this project

### Stuff to do
4. Accept the POST request in Flask, and look into it
5. Use logsol's [Github-Auto-Deploy](https://github.com/logsol/Github-Auto-Deploy) tool or write your own 
to accept a POST request from GitHub and update the local repo.


## Notes:
1. We won't be editing any of the files from the production server.

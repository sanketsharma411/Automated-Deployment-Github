# flask-api-test
Testing automated deplolyment through GitHub's Post-receive hooks



### Done 
1. Create a basic Flask App
2. Serve it through gunicorn on AWS EC2 instance
3. Setup a GitHub post-receive hook for this project
4. Accept the POST request in Flask, and look into it

### Stuff to do

5. Create a bash script which updates the local repo 
6. Run the bash script whenever a "message" is received from GitHub


## Notes:
1. We won't be editing any of the files from the production server.


The post receive hook delivers some payload thing which is not a part of the request.args but is instead a component 
of request.dataStatus API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy Security Contact Help
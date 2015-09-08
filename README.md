# flask-api-test
Testing automated deplolyment through GitHub's Post-receive hooks



### Done 
1. Create a basic Flask App
2. Serve it through gunicorn on AWS EC2 instance
3. Setup a GitHub post-receive hook for this project
4. Accept the POST request in Flask, and look into it

### Stuff to do

5. Create a bash script which updates the local repo 
6. Verify/validate the "message" received from GitHub
7. Run the bash script from python
8. Low Priority : Convert it to a nice utility such that it can be used with any project


## Notes:
- We won't be editing any of the files from the production server, so no conflicts 
and it will always pull from the origin/master branch
- The post receive hook delivers some payload thing which is not a part of the request.args but is instead a component 
of request.data
- The only way we are using the post-recieve hooks now is to tell the server to "git pull". This __should__ be extended later !

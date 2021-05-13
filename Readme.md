# Credentials
Before you can deploy this application, be sure you have credentials configured. If you have previously configured your machine to run boto3 (the AWS SDK for Python) or the AWS CLI then you can skip this section.

If this is your first time configuring credentials for AWS you can follow these steps to quickly get started:

$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)


# To Deploy
`chalice deploy`

See documentation [here](http://aws.github.io/chalice/) for more information

# To Run Locally

-  Create an virtual env 
-  Install requirements
-  Run `chalice local`

# To Run Test

Run `python -m unittest tests.py`

# To Run Script

Run `python section_one.py`
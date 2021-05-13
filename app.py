from datetime import datetime
import os
import csv
import urllib

from chalice import Chalice, Rate

import boto3
import requests

app = Chalice(app_name="cognetiks")
app.debug = True
now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# variables
BUCKET_NAME = "your-bucket-name"
TABLE_NAME = "your-dynamodb-table-name"


# Automatically runs every 24 hours
@app.schedule(Rate(24, unit=Rate.HOURS))
def periodic_task(event):
    '''
    A lambda function that reads data from an API, stores `states` data from the API in csv format
    as an object in an S3 bucket using the timestamp as the object key.
    '''

    title = 'covid-data-{}.csv'.format(now)
    temp_path = os.path.join("/tmp/", title)

    response = requests.get('https://covidnigeria.herokuapp.com/api').json()
    data = response['data']['states']

    header = data[0].keys()

    # write api response to csv file
    with open(temp_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for d in data:
            writer.writerow(d.values())
        
    # upload to s3
    s3_resource = boto3.resource('s3')
    s3_resource.Bucket(BUCKET_NAME).upload_file(
                    Filename=temp_path, 
                    Key=title, 
                    ExtraArgs={'ACL': 'public-read'}
                )

    # generate object url
    object_url = urllib.parse.quote(f"{BUCKET_NAME}.s3.amazonaws.com/{title}")

    # store url object in dynamodb
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.put_item(
                    TableName=TABLE_NAME,
                    Item={
                        'url': {
                            'S': f'{object_url}',
                        }
                    },   
                )
    return {"success": "true"}




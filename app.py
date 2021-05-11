from datetime import datetime
import os
import csv

from chalice import Chalice, Rate

import boto3
import requests

app = Chalice(app_name="cognetiks")
now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


# Rate.
# Automatically runs every 5 minutes
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    '''
    Reads data from an API, stores `states` data from the API in csv format
    as an object in an S3 bucket using the timestamp as the object key.
    '''

    title = 'covid-data-{}.csv'.format(now)
    temp_path = os.path.join("/tmp/", title)

    response = requests.get('https://covidnigeria.herokuapp.com/api').json()
    data = response['data']['states']

    header = data[0].keys()

    with open(temp_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for d in data:
            writer.writerow(d.values())
        
    bucket_name = "your-bucket-name"
    s3_resource = boto3.resource('s3')
    s3_resource.Bucket(bucket_name).upload_file(
        Filename=temp_path, Key=now, ExtraArgs={'ACL': 'public-read'})

    return {"success": "true"}




from __future__ import print_function

import json
import boto3

print('Loading function')

s3c = boto3.client('s3')

def lambda_handler(event, context):
    
    # Get NEXRAD data from it's S3 bucket
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    keyFile = key.replace("/","_")
    
    try:
        response = s3c.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        
        download_path = keyFile
        upload_path = keyFile
        s3c.download_file(bucket, key, download_path)
        
        #s3c.upload_file(download_path, 'data-eng-project', 'stream/' + download_path)
        return response['ContentType']
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e
        
    # s3c.download_file("data-eng-project", "fig1.png", "fig1.png")
    
    # data = open('fig.png', 'rb')
    
    # s3r = session.resource('s3')
    # s3r.Bucket('data-eng-project').put_object(Key='stream/fig.png', Body=data)

    #s3.Object('data-eng-project', 'hello.txt').put(Body=data)
    #s3.Bucket('data-eng-project').put_object(Key='stream/bar.txt', Body=message)
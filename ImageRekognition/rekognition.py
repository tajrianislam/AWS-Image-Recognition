import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'hot_air_balloon.jpeg'

client = boto3.client('rekognition', 
                                aws_access_key_id = access_key_id, 
                                aws_secret_access_key = secret_access_key, 
                                region_name='us-west-2')

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes': source_bytes}, MaxLabels=10, MinConfidence=90)

#Retrieving from S3 bucket
#  Image={
#         'Bytes': b'bytes',
#         'S3Object': {
#             'Bucket': 'string',
#             'Name': 'string',
#             'Version': 'string'
#         }

#Additional functionality
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels


print(response)
#return JSON object with elements in image along with their recognition %



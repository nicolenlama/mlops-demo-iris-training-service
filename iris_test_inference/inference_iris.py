# %%
import pickle
import boto3
import pandas as pd
import numpy as np
from datetime import date

# Uses the creds in ~/.aws/credentials
access_key = 'cIyf0MjSsGhuTUKjhe1U'
secret_key = 'cgBmTl2kitRoXl2/G6foGaKV8hVSoo7/Ih0W86My'
endPoint= 's3.openshift-storage.svc:443'
service_point = 'http://s3.openshift-storage.svc.cluster.local'
bucketName = 'bucket--8a865306-d4ec-453b-ab70-e8cd62ab835e' 
#fileName = fileName = f'../temp_models/iris-model_{date}.pkl' 
s3client = boto3.client('s3','us-east-1', endpoint_url=service_point,
                       aws_access_key_id = access_key,
                       aws_secret_access_key = secret_key,
                        use_ssl = True if 'https' in service_point else False,
                       verify = False)


objects = s3client.list_objects_v2(Bucket=bucketName)


allFiles = []
for obj in objects['Contents']:
    print(obj['Key'])
    allFiles.append(obj['Key'])

print(allFiles)
allFiles.sort()
fileName = allFiles[0]
s3client.download_file(
    Bucket=bucketName, Key=fileName, Filename="./model"
)
obj = open("./model", "rb")
model = pickle.load(obj)
print(model.predict([[5,3,1.6,0.2]]))

#s3client.upload_file(fileName, bucketName, fileName)

# some time later...
 
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
#print(result)

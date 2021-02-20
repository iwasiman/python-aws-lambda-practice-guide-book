for rec in event['Records']:
    print(rec['s3']['object']['key'])


s3 = boto3.resource('s3')
s3_obj = s3.Object('バケット名', 'ファイル名')

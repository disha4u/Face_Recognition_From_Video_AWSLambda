import boto3
import os

class S3(object):

    aws_access_key_id = 'AKIA3G6GKCEDZRM2IIQO'
    aws_secret_access_key = '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'
    s3=boto3.client('s3',aws_access_key_id=aws_access_key_id,  aws_secret_access_key=aws_secret_access_key,region_name='us-east-1')


    @staticmethod
    def find_bucket(name):
        all_buckets=S3.s3.list_buckets().get('Buckets')
        for bucket in all_buckets:
            print(bucket['Name'])
            if bucket['Name']==name:
                return True
        return False
    
    @staticmethod
    def create_bucket(name):
        S3.s3.create_bucket(Bucket=name,CreateBucketConfiguration={'LocationConstraint': 'us-east-1a'})
    
    @staticmethod
    def add_object(name,key,value):
        S3.s3.put_object(Body=value,Bucket=name, Key=key)

    @staticmethod
    def upload_file(name,filename,filepath):

        S3.s3.upload_file(Filename=filepath, Bucket=name,Key=filename)

    @staticmethod
    def read_file(name,key,download_path):
        S3.s3.download_file(Bucket=name,Key=key,Filename=download_path+key)
        
    
    @staticmethod
    def read_object(name,key):
        dc=S3.s3.get_object(Bucket=name,Key=key)
        return dc['Body']

    @staticmethod
    def get_num_objects(name):
        resp = S3.s3.list_objects_v2(Bucket=name)
        count=0
        for obj in resp['Contents']:
            if obj['Size'] != 0:
                count+=1
        return count
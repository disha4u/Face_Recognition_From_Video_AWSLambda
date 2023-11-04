#from boto3 import client as boto3_client
import face_recognition
import pickle
import os
from urllib.parse import unquote_plus
from s3_utils import S3
import boto3

aws_access_key_id = 'AKIA3G6GKCEDZRM2IIQO'
aws_secret_access_key = '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'
dbclient=boto3.client("dynamodb",aws_access_key_id=aws_access_key_id,  aws_secret_access_key=aws_secret_access_key,region_name='us-east-1')

input_bucket = "cc-p2-input-bucket"
output_bucket = "cc-p2-output-bucket"

name_id={'president_obama': '7','johnny_dep': '8','vin_diesel': '3','president_biden': '2',
         'floki': '4','morgan_freeman': '6','mr_bean': '1','president_trump': '5'}


def dynamodb_util(name):
    id=name_id[name]
    query=f"SELECT major,year FROM project2_lambda WHERE id={id}"
    res=dbclient.execute_statement(Statement=query)

    res_string=f"{res["Items"]["major"]["S"]},{res["Items"]["year"]["S"]}"
    return res_string

# def download_video_file(key,path):
# 	S3.read_file(input_bucket,key,path)

# Function to read the 'encoding' file
def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data
#(event, context):	
def face_recognition(im,data):
    unknown_pic = face_recognition.load_image_file(im)
    unknown_encoding = face_recognition.face_encodings(unknown_pic)[0]
    for i,enc in enumerate(data["encoding"]):
        results = face_recognition.compare_faces([enc], unknown_encoding)
        if results[0] == True:
            print("It's a picture of "+data["name"][i])
            return data["name"][i]
            break
        print("nothing found")
    return ""

def main_handler(event,context):
    for record in event['Records']:
        #bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        key=key.replace("/","")
        download_path = './video/'
        S3.read_file(input_bucket,key,download_path)
        path=get_images(download_path+key)
        data=open_encoding("encoding")
        f=face_recognition(path,data)
        res=dynamodb_util(f)
        final_res=f"{key}:{res}"
        S3.add_object(output_bucket,key,final_res)
        
        


def get_images(video_path):
	path="./tmp/"
	os.system("ffmpeg -i " + str(video_path) + " -r 1 " + str(path) + "image-%3d.jpeg")
	return path+"image-001.jpeg"


# if __name__=="__main__":
#     d=open_encoding("encoding")
#     #print(d)
#     face_recognition_handler("./tmp/image-001.jpeg",d)
#     #vid="/home/disha4u/cloud/test_0.mp4"
# 	#im=get_images(vid)
	
	


from boto3 import client as boto3_client
import face_recognition
import pickle,os
import configparser
import boto3,sys,uuid
config = configparser.ConfigParser()
config.read(".env")

# print(config.keys())
input_bucket = config['Buckets']['input_bucket']
output_bucket = config['Buckets']['output_bucket']
aws_access_key_id=config['Credentials']['aws_access_key_id']
aws_secret_access_key=config["Credentials"]["aws_secret_access_key"]
# Function to read the 'encoding' file
s3=boto3.client('s3',aws_access_key_id=aws_access_key_id,  aws_secret_access_key=aws_secret_access_key,region_name='us-east-1')
# print("Created S3 client")


dbclient=boto3.client("dynamodb",aws_access_key_id=aws_access_key_id,  aws_secret_access_key=aws_secret_access_key,region_name='us-east-1')
name_id={'president_obama': '7','johnny_dep': '8','vin_diesel': '3','president_biden': '2',
         'floki': '4','morgan_freeman': '6','mr_bean': '1','president_trump': '5'}


def dynamodb_util(name):
	id=int(name_id[name])
	query=f"SELECT major,year FROM project2_lambda WHERE id={id}"
	res=dbclient.execute_statement(Statement=query)
	res_string=f'{res["Items"][0]["major"]["S"]},{res["Items"][0]["year"]["S"]}'
	return res_string


def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data
	
def face_recognition_1(im,data):
	unknown_pic = face_recognition.load_image_file(im)
	unknown_encoding = face_recognition.face_encodings(unknown_pic)[0]
	for i,enc in enumerate(data["encoding"]):
		results = face_recognition.compare_faces([enc], unknown_encoding)
		if results[0] == True:
			return data["name"][i]
			break
		print("nothing found")
	return ""


def get_images(video_path):
	path="/tmp/images/"
	if not os.path.exists("/tmp/images/"):
		os.mkdir("/tmp/images/")
	os.system("ffmpeg -i " + str(video_path) + " -r 1 " + str(path) + "image-%3d.jpeg")
	return path+"image-001.jpeg"



def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data

def face_recognition_handler(event, context):
	try:
		key = event['Records'][0]['s3']['object']['key']
		s3.download_file(input_bucket, key, "/tmp/"+key)
		path=get_images("/tmp/"+key)
		data=open_encoding("encoding")
		f=face_recognition_1(path,data)
		res=dynamodb_util(f)
		final_res=f"{f},{res}"
		key=key[0:-4]
		os.system(f"echo {final_res} >> /tmp/{key}.csv")
		# print("/tmp/"+key+".csv",os.path.exists("/tmp/"+key+".csv"))
		s3.upload_file(Filename="/tmp/"+key+".csv", Bucket=output_bucket,Key=key+".csv")
		# s3.put_object(Bucket=output_bucket, Key=key[0:-4], Body=final_res)
		print("Uploaded the Object in ",output_bucket)
			
	except Exception as e:
		print(e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)
	finally:
	  	return "Hello World!!!!!!"
# face_recognition_handler()
# dynamodb_util("president_obama")	
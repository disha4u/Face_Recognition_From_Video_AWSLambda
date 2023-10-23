#from boto3 import client as boto3_client
import face_recognition
import pickle
import os
#from s3_utils import S3

input_bucket = "546proj2"
output_bucket = "546proj2output"


# def download_video_file(key,path):
# 	S3.read_file(input_bucket,key,path)

# Function to read the 'encoding' file
def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data
#(event, context):	
def face_recognition_handler(im,data):
    unknown_pic = face_recognition.load_image_file(im)
    unknown_encoding = face_recognition.face_encodings(unknown_pic)[0]
    for i,enc in enumerate(data["encoding"]):
        results = face_recognition.compare_faces([enc], unknown_encoding)
        if results[0] == True:
            print("It's a picture of "+data["name"][i])
            break
        
	

def get_images(video_path):
	path="./tmp/"
	os.system("ffmpeg -i " + str(video_path) + " -r 1 " + str(path) + "image-%3d.jpeg")
	return path+"image-001.jpeg"


if __name__=="__main__":
    d=open_encoding("encoding")
    #print(d)
    face_recognition_handler("./tmp/image-001.jpeg",d)
    #vid="/home/disha4u/cloud/test_0.mp4"
	#im=get_images(vid)
	
	


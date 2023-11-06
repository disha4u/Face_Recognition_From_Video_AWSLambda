#Elastic Application - Face Recognition & Retrieve data from DynamoDB using AWS Lambda

##About the Project

####Code Strucutre
├── Readme.md
├── handler.py
├── DockerFile
├── encoding
├── entry.sh
├── requirements.txt
└── workload_generator


## Getting Started

There are 

```
pip3 install -r requirements.txt
```

For running the main flask server:

```
cd /home/ec2-user/Cloud_Project1
nohup python web_server.py &
```

For running the controller script to perform auto-scaling:

```
cd /home/ec2-user/Cloud_Project1
python3 appScaler.py
```

For running the app-tier code, first install the dependancies using pip.
Use amiID ami-0d5865d3d6fffbdb2 to launch the instance

```
cd /home/ubuntu/app-tier
python3 main.py
```


<!-- LICENSE -->

#### Team Members

1. Ramchandra Sai- Worked on creating trigger and docker image , uploading it to ECR.
2. Disha Agarwal - Worked on lambda function parts face recognition, video splitting and retrieving info from dynamodb.
3. Sanket Duhoon - Worked on creating dynamodb database, querying database, and fixing bugs in handler.py.

##### AWS Resources

- AWS Credentials are provided in the Excel file.

- The PEM key file is added to the submission.
  IMAGE_BUCKET = 'cc-p2-input-bucket'
  OUTPUT_BUCKET = 'cc-p2-output-bucket'

